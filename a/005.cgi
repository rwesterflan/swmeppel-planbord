#!/usr/bin/perl -w
print "Content-type: text/html\n\n"; #Timelife classics

########################################################################### Post-processing
use Carp;
use CGI;			
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use DBI();
use Digest::SHA qw(sha1 sha1_hex);
use Date::Manip;

########################################################################### Create stack
if ($ENV{'REQUEST_METHOD'} eq 'POST') {
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@000 = split(/&/, $buffer); } else { @000 = split(/&/, $ENV{'QUERY_STRING'}); }
foreach $000 (@000) {
($001, $002) = split (/=/, $000);
$001 =~ tr/+/ /;
$001 =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$001 =~ s/\'/\\\'/g; 
$001 =~ s/\"/\\\"/g;
$002 =~ tr/+/ /;
$002 =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$002 =~ s/\'/\\\'/g; 
$002 =~ s/\"/\\\"/g;
$002 =~ s/[\n]/<br>/g;
if($out{request} =~ /^00t$/){ 
} else {
$002 =~ s/<br><br>/<br>/g; #doubles
$002 =~ s/<br><tr>/<tr>/g; #doubles
$002 =~ s/<br><table>/<table>/g; #doubles
$002 =~ s/<br><\/table>/<\/table>/g; #doubles
};
{ $out{$001} = $002; } };

require "dbd.cfg"; 
 
########################################################################### 00b
if($out{request} =~ /^00b$/){
$dbh->do("INSERT INTO enqv2 VALUES ('', '$out{courseID}', '$out{courseDate}', '$out{werkplek}', '$out{sfeer}', '$out{comf}', '$out{tempo}', '$out{topics}', '$out{mats}', '$out{expl}', '$out{hulp}', '$out{prep}', '$out{thuis}', '$out{com1}', '$out{com2}', '$out{com3}', '$out{com4}', '$out{com5}', '$out{courseRef}', '$out{courseTeacher}', '$out{future}')");

$targetURL="01b";
};

########################################################################### Finishing touch
print "<script type=\"text/javascript\">  window.location.href = \"../enq.cgi?fn=$targetURL\";</script>";
print "Klik <a href=../?fn=$targetURL>hier</a> als je niet word doorverwezen...";
