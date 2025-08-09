import sqlite3
import pandas as pd

# Ulash
conn = sqlite3.connect("chinook.db")

# So'rov
query = """
SELECT 
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    SUM(i.Total) AS TotalSpent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5;
"""

# So‘rovni bajarish
top_customers_df = pd.read_sql_query(query, conn)

# Natijani ko‘rish
print(top_customers_df)

# Ulanishni yopish
conn.close()

conn = sqlite3.connect('chinook.db')
query="""

WITH AlbumTrackCounts AS (
  SELECT AlbumId, COUNT(*) AS TotalTracks
  FROM Track
  GROUP BY AlbumId
),


CustomerAlbumTrackPurchases AS (
  SELECT 
    c.CustomerId,
    t.AlbumId,
    COUNT(DISTINCT t.TrackId) AS PurchasedTracks
  FROM Customer c
  JOIN Invoice i ON c.CustomerId = i.CustomerId
  JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
  JOIN Track t ON il.TrackId = t.TrackId
  GROUP BY c.CustomerId, t.AlbumId
),


CustomerAlbumPurchaseType AS (
  SELECT 
    catp.CustomerId,
    catp.AlbumId,
    CASE 
      WHEN catp.PurchasedTracks = atc.TotalTracks THEN 1
      ELSE 0
    END AS IsFullAlbum
  FROM CustomerAlbumTrackPurchases catp
  JOIN AlbumTrackCounts atc ON catp.AlbumId = atc.AlbumId
),


CustomerPreference AS (
  SELECT 
    CustomerId,
    MAX(IsFullAlbum) AS BoughtFullAlbum
  FROM CustomerAlbumPurchaseType
  GROUP BY CustomerId
)


SELECT
  SUM(CASE WHEN BoughtFullAlbum = 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Percent_Individual_Track_Customers,
  SUM(CASE WHEN BoughtFullAlbum = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Percent_Album_Customers
FROM CustomerPreference;

"""
customers_track = pd.read_sql_query(query, conn)

print(customers_track)
conn.close()

