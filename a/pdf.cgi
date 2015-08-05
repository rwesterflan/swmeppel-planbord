#!/usr/bin/perl -w
########################################################################### Post-processing
use CGI;			
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use DBI();

print "Content-type: text/html\n\n";

########################################################################### DBI calls
if ($ENV{'REQUEST_METHOD'} eq 'POST') {
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@000 = split(/&/, $buffer); } else { @000 = split(/&/, $ENV{'QUERY_STRING'}); }
foreach $000 (@000) {
($001, $002) = split (/=/, $000);
$001 =~ tr/+/ /;
$001 =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$002 =~ tr/+/ /;
$002 =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
{ $out{$001} = $002; } };

$session = CGI::Session->load() or die CGI::Session->errstr();
$CGISESSION = $session->id();
if(!$CGISESSION) { print "<script type=text/javascript>  window.location.href = \"../admin.cgi\";</script> "; exit; };
$domain = $session->param('domain');

require ("dbd.cfg");

########################################################################### Load shizzle
if($out{filter} =~ /doc/){
$Pag = $dbh->prepare("SELECT * FROM users where swtask like '%doc%' order by lname");
$f1a = "<b>";
$f2a = "</b>";
}elsif($out{filter} =~ /other/){
$Pag = $dbh->prepare("SELECT * FROM users where swtask like '%other%' order by lname");
$f1c = "<b>";
$f2c = "</b>";
}elsif($out{filter} =~ /ass/){
$Pag = $dbh->prepare("SELECT * FROM users where swtask like '%ass%' order by lname");
$f1b = "<b>";
$f2b = "</b>";
}elsif($out{filter} =~ /^meppel/){
$Pag = $dbh->prepare("SELECT * FROM users where city like '%Meppel%' order by lname");
$f1e = "<b>";
$f2e = "</b>";
}elsif($out{filter} =~ /^hoogeveen/){
$Pag = $dbh->prepare("SELECT * FROM users where city like '%Hoogeveen%' order by lname");
$f1h = "<b>";
$f2h = "</b>";
}elsif($out{filter} =~ /^staphorst/){
$Pag = $dbh->prepare("SELECT * FROM users where city like '%Staphorst%' order by lname");
$f1i = "<b>";
$f2i = "</b>";
}elsif($out{filter} =~ /^neverland/){
$Pag = $dbh->prepare("SELECT * FROM users where city not in ('Meppel') order by lname");
$f1j = "<b>";
$f2j = "</b>";
}elsif($out{filter} =~ /^female/){
$Pag = $dbh->prepare("SELECT * FROM users where title like '%Mw%' order by lname");
$f1f = "<b>";
$f2f = "</b>";
}elsif($out{filter} =~ /^male/){
$Pag = $dbh->prepare("SELECT * FROM users where title like '%Dhr%' order by lname");
$f1g = "<b>";
$f2g = "</b>";
} else {
$Pag = $dbh->prepare("SELECT * FROM users order by lname");
$f1d = "<b>";
$f2d = "</b>";
};

$Pag->execute();

if(!$out{footer}){ $out{footer} = "Werk deze gegevens bij via <b>http://planbord.swmeppel.nl</b>"; };
if(!$out{header}){ $out{header} = "Seniorweb Meppel - Presentielijst"; };
if(!$out{hdrFontSize}){ $out{hdrFontSize} = "6"; };
if($out{hideFilter}){ $hidfil = "checked"; };


########################################################################### THIS IS AWESOME (Do not touch, it might bite).
print <<DURR;
<html>
<head>
<link rel="stylesheet" type="text/css" href="./pdf.css"/> 
<title>Seniorweb Meppel - Planning and control</title>

<style>
tr:nth-child(odd) {background: #ddd}
tr:nth-child(even) {background: #eee}
</style>
</head>

<body>
<font face=Arial>
<div class=sheet>
<center><font size=$out{hdrFontSize}><b>$out{header}</b></font><br>
DURR

if(!$out{hideFilter}){
print "<u><font size=2>Filter: <a href=?fn=00n&filter=doc> $f1a Docenten $f2a </a> / <a href=?fn=00n&filter=ass> $f1b assistenten $f2b </a> / <a href=?fn=00n&filter=other> $f1c overige taken $f2c </a> | <a href=?fn=00n&filter=meppel> $f1e Uit Meppel $f2e</a> / <a href=?fn=00n&filter=neverland> $f1j of daarbuiten $f2j</a>| <a href=?fn=00n&filter=female> $f1f Vrouwen $f2f </a> / <a href=?fn=00n&filter=male> $f1g mannen $f2g </a> | <a href=?fn=00n> $f1d Geen filter $f2d </a></u><br>";
};

print <<DURR;
</center>
<div class=declare>
<font size=2>
<table border="0" cellspacing=0>
DURR

while (@naw = $Pag->fetchrow()) {


if($naw[15] =~ /^ass$/){ $txlbl = "Assistent"; }; 
if($naw[15] =~ /^doc$/){ $txlbl = "Docent"; };
if($naw[15] =~ /^docass$/){ $txlbl = "Docent/assistent"; };
if($naw[15] =~ /^other$/){ $txlbl = "Iets anders"; };
if($naw[12]){ $txlbl = $txlbl.", ".$naw[12]; };
if($naw[0] != "998"){ #sorry Flan
 print "<tr><td width=20px><input type=checkbox></td><td width=60px>$naw[2]</td><td width=170px>$naw[4] <b>$naw[5]</b></td><td width=100px></td><td width=280px>$txlbl</td></tr>\n";
};
$txlbl = "";
}

print <<DURR;
<tr><td colspan=5 align=center>$out{footer}</td></tr>
</table>
</div>
</div>
<p><hr><p>
<h2>Formulieropties</h2>
Dit document is gemaakt om precies op 1 A4tje te passen. <br>
De kop en voettekst van deze pagina kunnen worden aangepast (bijvoorbeeld voor een korte mededeling).<br>
Denk aan iets als 'Prettige kerstdagen!'. Zie het voorbeeld, en gebruik de volgende opmaaktekens:<br>
&lt;b&gt; ... &lt;/b&gt; = <b>dikgedrukt</b><br>
&lt;u&gt; ... &lt;/u&gt; = <u>onderstreep</u><br>
&lt;i&gt; ... &lt;/i&gt; = <i>cursief</i><br>
&lt;font color=KLEUR&gt; ... &lt;/font&gt; = kies een kleur, in het engels. Bijvoorbeeld <font color=red>red</font>, <font color=blue>blue</font> of <font color=green>green</font>
<p>
<form  action=pdf.cgi method=post>
<input type=hidden name=filter value="$out{filter}">
Koptekst: <input type=text style="width:535px;" name=header value="$out{header}"> - lettergrootte <input type=text style="width:35px;" name=hdrFontSize value="$out{hdrFontSize}"> punten<br>
Voettekst: <input type=text style="width:535px;" name=footer value="$out{footer}"><br>
<input type=checkbox name=hideFilter $hidfil> Verberg filteropties (dit geeft een extra regel voor de voettekst, maar het kan handig zijn om op de lijst te laten staan hoe deze geprint is)<br>
<input type=submit value=Bijwerken></form>
<p>
Let op bij het afdrukken: druk alleen pagina 1 af, en vergeet de achtergrondkleuren niet.
</body>
</html>
DURR


