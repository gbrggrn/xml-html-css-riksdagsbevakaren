<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:custom="http://riksdagsinfo.se/votes">
<!-- Filename: staff_cards.xsl -->
<!-- Author: Gustaf Berggren Sörlin -->
<!-- Date: 2026-05-03 -->

    <xsl:template match="staff">

        <xsl:variable name="current_iid" select="normalize-space(iid)"/>

        <a href="#modal-{$current_iid}" class="card-link">
            <div class="card" data-party="{party}">
                <img src="{img_url}" alt="Profilbild"/>
                <h3><xsl:value-of select="name/first_name"/>&#160;<xsl:value-of select="name/last_name"/></h3>
                <span class="party-badge"><xsl:value-of select="party"/></span>
            </div>
        </a>

        <div id="modal-{$current_iid}" class="modal-overlay">
            <div class="modal-content">
                <a href="#" class="close-btn">&#215;</a>
                
                <div class="modal-header">
                    <img src="{img_url}"/>
                    <h2><xsl:value-of select="name/first_name"/>&#160;<xsl:value-of select="name/last_name"/></h2>
                    <span class="party-badge"><xsl:value-of select="party"/></span>
                </div>

                <div class="modal-body">
                    <div class="assignments">
                        <h3>Uppdrag</h3>
                        <ul>
                            <xsl:for-each select="assignments/assignment">
                                <li><xsl:value-of select="from"/> - <xsl:value-of select="to"/> | <xsl:value-of select="role"/> | <xsl:value-of select="task"/></li>
                            </xsl:for-each>
                        </ul>
                    </div>

                    <div class="motions">
                        <h3>Senaste motioner</h3>
                        <ul>
                            <xsl:for-each select="$docs_data//doc[normalize-space(iid) = $current_iid]">
                                <li><a href="{dok_url}" target="_blank"><xsl:value-of select="title"/></a></li>
                            </xsl:for-each>
                        </ul>
                    </div>

                    <div class="votes">
                        <h3>Senaste voteringar</h3>
                        <ul>
                            <xsl:for-each select="$votes_data//vote[normalize-space(iid) = $current_iid]">
                                <li><a href="{custom:url}" target="_blank"><xsl:value-of select="custom:title"/></a>, punkt <xsl:value-of select="point"/>: <xsl:value-of select="result"/></li>
                            </xsl:for-each>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </xsl:template>
    
</xsl:stylesheet>