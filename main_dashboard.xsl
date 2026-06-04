<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- Filename: main_dashboard.xsl -->
<!-- Author: Gustaf Berggren Sörlin -->
<!-- Date: 2026-05-03 -->
<xsl:include href="staff_cards.xsl"/>

    <xsl:output method="html" doctype-system="about:legacy-compat" encoding="UTF-8" indent="yes"/>

    <xsl:variable name="staff_data" select="document(/riks_data/riks_staff/@file)"/>
    <xsl:variable name="docs_data" select="document(/riks_data/riks_docs/@file)"/>
    <xsl:variable name="votes_data" select="document(/riks_data/riks_votes/@file)"/>

    <xsl:template match="/riks_data">    
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title><xsl:value-of select="title"/></title>
                <link rel="stylesheet" href="style.css"/>
            </head>

            <body>
                <div class="dashboard-main">
                    <h1><xsl:value-of select="title"/></h1>
                    <p>Skapad av: <xsl:value-of select="author"/></p>
                    <div class="stats-panel">
                        <div class="stats-box">Totalt antal ledamöter: <xsl:value-of select="count($staff_data//staff)"/></div>
                    </div>
                </div>

                <div class="netflix-row">
                    <h2>Aktuella ledamöter</h2>
                    <div class="netflix-grid">
                        <xsl:apply-templates select="$staff_data//staff"/>
                    </div>
                </div>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>