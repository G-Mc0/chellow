<?xml version="1.0" encoding="us-ascii"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" encoding="US-ASCII"
		doctype-public="-//W3C//DTD HTML 4.01//EN"
		doctype-system="http://www.w3.org/TR/html4/strict.dtd" indent="yes" />

	<xsl:template match="/">
		<html>
			<head>
				<link rel="stylesheet" type="text/css"
					href="{/source/request/@context-path}/orgs/{/source/contracts/org/@id}/reports/9/stream/output/" />
				<title>
					<xsl:value-of select="/source/contracts/org/@name" />
					&gt; Market Roles
				</title>
			</head>
			<body>
				<p>
					<a
						href="{/source/request/@context-path}/orgs/{/source/roles/org/@id}/reports/0/screen/output/">
						<xsl:value-of select="/source/roles/org/@name" />
					</a>
					&gt;
					<xsl:value-of select="'Market Roles'" />
				</p>
				<br />
				<xsl:if test="//message">
					<ul>
						<xsl:for-each select="//message">
							<li>
								<xsl:value-of select="@description" />
							</li>
						</xsl:for-each>
					</ul>
				</xsl:if>
				<table>
					<thead>
						<tr>
							<th>Chellow Id</th>
							<th>Code</th>
							<th>Description</th>
						</tr>
					</thead>
					<tbody>
						<xsl:for-each
							select="/source/roles/market-role">
							<tr>
								<td>
									<a
										href="{/source/request/@context-path}/orgs/{/source/roles/org/@id}/reports/61/screen/output/?role-id={@id}">
										<xsl:value-of select="@id" />
									</a>
								</td>
								<td>
									<xsl:value-of select="@code" />
								</td>
								<td>
									<xsl:value-of select="@description" />
								</td>
							</tr>
						</xsl:for-each>
					</tbody>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>