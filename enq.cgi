#!/usr/bin/perl -w
########################################################################### Post-processing
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use DBI();
use Data::Dumper;

########################################################################### 
########################################################################### Userconfig
$titelbalk="Seniorweb Meppel Planbord - v1.1";
$titelkleur="3399FF";
$menukleur="119BCF"; #6699FF is 'n lichtere blauw

########################################################################### Datum/Tijd
@months = qw(01 02 03 04 05 06 07 08 09 10 11 12);
@weekDays = qw(Zo Ma Di Wo Do Vr Za Zo);
($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = localtime();
$year = 1900 + $yearOffset;
if($minute <= "9"){ $minute="0$minute" }; 
if($dayOfMonth <= "9"){ $dayOfMonth="0$dayOfMonth" }; 
$tijd = "$hour:$minute";
$datum = "$dayOfMonth-$months[$month]-$year";
$sqldate = $year.$months[$month].$dayOfMonth;

require "a/dbd.cfg"; 

print "Content-type: text/html\n\n"; #HTML header
########################################################################### 
########################################################################### Schrijf eerste stuk HTML
print "<html>";
print "<head>";
print <<FIRSTHTML;
<link rel="stylesheet" type="text/css" href="./style.css"/>
<title>$titelbalk</title>
</head>
<body bgcolor=black>
<p>
<table bgcolor=#eee cellspacing=0 border=0>
<tr><td bgcolor=$titelkleur height=30 colspan=2><font face=Arial color=white size=3><b>Seniorweb Meppel Enquete</b></td></tr>
<tr>
FIRSTHTML

print "<td bgcolor=$menukleur width=117px height=231 valign=top>";
print "<td bgcolor=#EEEEEE valign=top border=0 width=883 style=\"padding-left: 20px; padding-top: 10px; \"><font face=arial>";

require "a/00b";

$icanhasbutton="yes";
########################################################################### 
########################################################################### Schrijf laatste stuk HTML
print <<LASTHTML;
</td>
</tr>
<tr>
<td bgcolor=#CCCCCC width=1000 height=65 colspan=2 align=right>
LASTHTML

if($icanhasbutton =~ "yes"){
 print "<input type=submit value=Volgende\&gt>";
};

print <<LAPTEKST; 
</form></td>
</tr>
</table>
<font size=2 color=white><i>&copy 2012-$year Fland.re -- Code op <a style="color:white" href="https://git.fland.re/rwesterh/planbord">Gitlab</a></i></font>
</body>
</html>
LAPTEKST
