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

$Pag = $dbh->prepare("SELECT * FROM users order by lname");
$Pag->execute();

print <<WEE;
<html>
<head>
<link rel="stylesheet" type="text/css" href="./know.css"/> 
<title>Seniorweb Meppel - Planning and control</title>

<style>
tr:nth-child(odd) {background: #ddd}
tr:nth-child(even) {background: #eee}
</style>
</head>
<body>
<table border=0 cellpadding=0 cellspacing=0 class=sel width=610px>
WEE

$Tex= $dbh->prepare("SELECT id, icon, fullName FROM courses order by substr(id, 1, 2), fullName");
while (@naw = $Pag->fetchrow()) {
if($naw[0] != "998") { #sorry flan
$stattotal++;
#if($naw[0] == "999"){
 print "<tr></td><td nowrap>$naw[4] $naw[5]</b></td><td>";
$Tex->execute();

while (@der = $Tex->fetchrow()) {
if($naw[21]){ 
@000 = split(/&/, $naw[21]);
foreach $000 (@000) 
 {
 ($001, $002) = split (/=/, $000);
  { 
   $c{$001} = $002; 
  } 
 };

if($naw[21] =~ $der[0]){
  if($c{$der[0]} =~ /1/){ print "<img src=../content/static/ico/$der[1].png>"; };
  if($c{$der[0]} =~ /2/){ print "<img src=../content/static/ico/$der[1].png>"; }
  if($c{$der[0]} =~ /0/){ print "<img src=../content/static/ico/.png>"; }
} else { 
  if($c{$der[0]} =~ /0/){ print "<img src=../content/static/ico/.png>"; }
};
} else { print "<img src=../content/static/ico/.png>"; };
};
print "</td></tr>\n";

};
}
print "</table>";
print "</body></html>";
1;