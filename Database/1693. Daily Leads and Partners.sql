SELECT
    ds.date_id,
    ds.make_name,
    COUNT(DISTINCT ds.lead_id) AS unique_leads,
    COUNT(DISTINCT ds.partner_id) AS unique_partners
FROM DailySales AS ds
GROUP BY ds.date_id, ds.make_name
