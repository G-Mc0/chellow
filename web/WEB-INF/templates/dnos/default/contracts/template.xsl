<?xml version="1.0" encoding="us-ascii"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" encoding="US-ASCII"
		doctype-public="-//W3C//DTD HTML 4.01//EN" doctype-system="http://www.w3.org/TR/html4/strict.dtd"
		indent="yes" />
	<xsl:template match="/">
		<html>
			<head>
				<link rel="stylesheet" type="text/css"
					href="{/source/request/@context-path}/reports/19/output/" />
				<title>
					Chellow &gt; DNOs &gt;
					<xsl:value-of
						select="concat(/source/dno-contracts/dno/@code, ' &gt; Contracts')" />
				</title>
			</head>
			<body>
				<p>
					<a href="{/source/request/@context-path}/reports/1/output/">
						<xsl:value-of select="'Chellow'" />
					</a>
					&gt;
					<a href="{/source/request/@context-path}/reports/137/output/">
						<xsl:value-of select="'DNOs'" />
					</a>
					&gt;
					<a
						href="{/source/request/@context-path}/reports/139/output/?dno-id={/source/dno-contracts/dno/@id}">
						<xsl:value-of select="/source/dno-contracts/dno/@code" />
					</a>
					&gt; Contracts
				</p>

				<xsl:if test="//message">
					<ul>
						<xsl:for-each select="//message">
							<li>
								<xsl:value-of select="@description" />
							</li>
						</xsl:for-each>
					</ul>
				</xsl:if>
				<br />
				<form action="." method="post">
					<fieldset>
						<legend>Add a contract</legend>
						<br />
						<label>
							<xsl:value-of select="'Name '" />
							<input name="name"
								value="{/source/request/parameter[@name = 'name']/value}" />
						</label>
						<br />
						<br />
						<fieldset>
							<legend>Start Date</legend>
							<input name="start-year" maxlength="4" size="4">
								<xsl:attribute name="value">
											<xsl:choose>
												<xsl:when test="/source/request/parameter[@name='start-year']">
													<xsl:value-of
									select="/source/request/parameter[@name='start-year']/value" />
												</xsl:when>
												<xsl:otherwise>
													<xsl:value-of select="/source/date/@year" />
												</xsl:otherwise>
											</xsl:choose>
										</xsl:attribute>
							</input>
							<xsl:value-of select="'-'" />
							<select name="start-month">
								<xsl:for-each select="/source/months/month">
									<option value="{@number}">
										<xsl:choose>
											<xsl:when test="/source/request/parameter[@name='start-month']">
												<xsl:if
													test="/source/request/parameter[@name='start-month']/value = @number">
													<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
												</xsl:if>
											</xsl:when>
											<xsl:otherwise>
												<xsl:if test="/source/date/@month = @number">
													<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
												</xsl:if>
											</xsl:otherwise>
										</xsl:choose>
										<xsl:value-of select="@number" />
									</option>
								</xsl:for-each>
							</select>
							<xsl:value-of select="'-'" />
							<select name="start-day">
								<xsl:for-each select="/source/days/day">
									<option value="{@number}">
										<xsl:choose>
											<xsl:when test="/source/request/parameter[@name='start-day']">
												<xsl:if
													test="/source/request/parameter[@name='start-day']/value = @number">
													<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
												</xsl:if>
											</xsl:when>
											<xsl:otherwise>
												<xsl:if test="/source/date/@day = @number">
													<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
												</xsl:if>
											</xsl:otherwise>
										</xsl:choose>
										<xsl:value-of select="@number" />
									</option>
								</xsl:for-each>
							</select>
							<xsl:value-of select="' '" />
							<select name="start-hour">
								<xsl:for-each select="/source/hours/hour">
									<option value="{@number}">
										<xsl:choose>
											<xsl:when test="/source/request/parameter[@name='start-hour']">
												<xsl:if
													test="/source/request/parameter[@name='start-hour']/value = @number">
													<xsl:attribute name="selected"><xsl:value-of
														select="'selected'" />
													</xsl:attribute>
												</xsl:if>
											</xsl:when>
											<xsl:otherwise>
												<xsl:if test="/source/date/@hour = @number">
													<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
												</xsl:if>
											</xsl:otherwise>
										</xsl:choose>
										<xsl:value-of select="@number" />
									</option>
								</xsl:for-each>
							</select>
							<xsl:value-of select="':'" />
							<select name="start-minute">
								<xsl:for-each select="/source/hh-minutes/minute">
									<option value="{@number}">
										<xsl:if
											test="/source/request/parameter[@name='start-minute']/value = @number">
											<xsl:attribute name="selected">
																<xsl:value-of select="'selected'" />
															</xsl:attribute>
										</xsl:if>
										<xsl:value-of select="@number" />
									</option>
								</xsl:for-each>
							</select>
						</fieldset>
						<br />
						<br />
						<input type="submit" value="Add" />
						<input type="reset" value="Reset" />
					</fieldset>
				</form>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>