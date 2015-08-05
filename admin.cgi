#!/usr/bin/perl -w
########################################################################### Post-processing
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use DBI();
use Data::Dumper;
use Digest::SHA qw(sha1 sha1_hex);
use POSIX qw(ceil floor);

########################################################################### 
########################################################################### Userconfig
$titelbalk="Seniorweb Meppel Planbord - v1.1";
$titelkleur="3399FF";
$menukleur="119BCF"; #6699FF is 'n lichtere blauw

########################################################################### DBI calls
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
$002 =~ s/<br><br>/<br>/g; #doubles
$002 =~ s/<br><tr>/<tr>/g; #doubles
$002 =~ s/<br><table>/<table>/g; #doubles
$002 =~ s/<br><\/table>/<\/table>/g; #doubles
{ $out{$001} = $002; } };

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

########################################################################### DBI calls

#$FaIT = $dbh->prepare('SELECT * FROM config');
#$Dat = $dbh->selectall_hashref('SELECT * FROM config', 'naam');
#$FaIT->execute();


########################################################################### Sessiebeheer
$out{zzz} = "\L$out{zzz}";
$calcpass = sha1_hex("$out{zzy}_$out{zzz}");
$testdefault = sha1_hex("welkom123_$out{zzz}");
if($calcpass =~ /$testdefault/) { $defaultpasswordwarning = "1"; };

if($out{ibeloggingin} =~ /ye/){

$domain=$out{domain};

require "a/dbd.cfg"; 
 $User = $dbh->prepare('SELECT * FROM users');
 $user = $dbh->selectall_hashref('SELECT * FROM users', 'altusername');
 $User->execute();


 if($calcpass =~ /$user->{$out{zzz}}->{password}/){ $pass="1"; } else { $pass="0"; $loldong="<font color=red>Gebruikersnaam of wachtwoord onjuist (10029)</font>";};

 if(!$user->{$out{zzz}}->{id}){ $pass="0"; $loldong="<font color=red>Gebruikersnaam of wachtwoord onjuist (10028)!</font>"; };
 if(!$user->{$out{zzz}}->{password}){ $pass="0"; $loldong="<font color=red>Gebruikersnaam of wachtwoord onjuist (10027)</font>"; };
 if(!$user->{$out{zzz}}->{altusername}){ $pass="0"; $loldong="<font color=red>Gebruikersnaam of wachtwoord onjuist (10030!)</font>"; };

 if($calcpass =~ /^$/){$pass="0"; }; 
};

if($pass == "1"){
    $session = new CGI::Session() or die CGI::Session->errstr;
    $CGISESSION = $session->id();
    print $session->header();
    $session->param('user', $out{zzz});
    $session->param('level', $user->{$out{zzz}}->{elevation});
    $session->param('userid', $user->{$out{zzz}}->{id});
    $session->flush();
    $session->expire('+1h');
    $session->param('domain', $out{domain});
} else {
    $session = CGI::Session->load() or die CGI::Session->errstr();
    print "Content-type: text/html\n\n"; #HTML header
};

if($out{session} =~ /quit/){
    $session->delete();
    $session->flush(); 
};

$usrname = $session->param('user');
$level = $session->param('level');
$domain = $session->param('domain');
$userid = $session->param('userid');
$CGISESSION = $session->id();

require "a/dbd.cfg"; 

########################################################################### 
########################################################################### Schrijf eerste stuk HTML
print "<html>";
print "<head>";
if($out{fn} =~ /01h|00g/){
print <<JS;
<script language="javascript" type="text/javascript">
    function textareaKeyHook(sender, e) {
        var key = window.event ? window.event.keyCode : e.charCode ? e.charCode : e.which;
	if (e.ctrlKey && String.fromCharCode(key) == "I") { sender.value += "$datum $tijd ($usrname): "; return false; }
	return true;
}
</script>

JS

};

print <<FIRSTHTML;
<script type="text/javascript">
<!--
function init()
{
	if (!document.layers) return;
	var box = document.forms[0].elements;
	for (var i=0;i<box.length;i++)
	{
		box[i].disabled = true;
	}
}

function disableIt(obj)
{
	obj.disabled = !(obj.disabled);
	var z = (obj.disabled) ? 'enabled' : 'disabled';
}


function extracheck(obj)
{
	return !obj.disabled;
}
// -->
</script>
FIRSTHTML

if($out{autoupdate}=~/^1$/){
print <<JS;
<script type="text/javascript">
function reFresh() {
  location.reload(true)
}
window.setInterval("reFresh()",30000);
</script>
JS

$refrbtn= "Laatste update: $tijd";
}else{
$refrbtn= "<a href=\"admin.cgi?$ENV{'QUERY_STRING'}&autoupdate=1\"> <img src=./content/static/refresh.png style=border-style:none;></a>";
};

print <<FIRSTHTML;
<link rel="stylesheet" type="text/css" href="./style.css"/>
<title>$titelbalk</title>
</head>
<body bgcolor=black>
<p>
<table bgcolor=#3399FF cellspacing=0 border=0>
<tr>
 <td bgcolor=$titelkleur height=30 colspan=2><font face=Arial color=white size=3><b>$titelbalk</b></font><a href=admin.cgi?session=quit onclick="return confirm('Weet u zeker dat u zich af wilt melden?');"><img src=./content/static/end.png style=border-style:none; align=right></a></td>
</tr>
<tr>
FIRSTHTML

print "<td bgcolor=$menukleur width=117px height=231 valign=top>";
if(($CGISESSION =~ /^$/) || ($out{menu} =~ /off/)){
} else {
 if (-e "a/menu") { 
   require "a/menu" or die("Fout. Controleer of je goed bent aangemeld."); 
 } else {
 require "a/404"
 };
};

print "<td bgcolor=#CCCCCC valign=top border=0 width=883 style=\"padding-left: 20px; padding-top: 10px; \"><h1><font face=arial>";
########################################################################### 
########################################################################### Insert content
#if($ENV{'SERVER_PORT'} =~ /^2530$/){
#} else {
#print "</h1><font color=red><blink>Je probeert te verbinden via een onbeveiligde verbinding.<br>Let op dat Flopdesk tegenwoordig op poort 2530 zit. TCP. </blink><br><a href=https://192.168.0.248:2530/>Probeer opnieuw...</a>";
#exit;
#};

if($CGISESSION =~ /^$/){
$icanhasbutton="yes";

if($ENV{'SERVER_NAME'} =~ /enquete.swmeppel.nl/){
print <<LAPTEKST;
Welkom!</font></h1>
$loldong<br>
<font face=verdana>Klik op volgende om te beginnen.
<form action="admin.cgi" method="post">
<input type=hidden name=ibeloggingin value=ye>
<input type=hidden name=zzz value=enquete>
<input type=hidden name=zzy value=enquete>
<input type=hidden name=domain value=swmeppel>
<input type=hidden name=menu value=off>
<input type=hidden name=fn value=00b>


LAPTEKST

} else {

print <<LAPTEKST;
Welkom!</font></h1>
$loldong
<form action="admin.cgi" method="post">
<input type=hidden name=ibeloggingin value=ye><font face=verdana>
<table>
<tr><td>Gebruikersnaam:</td><td><input type="text" name="zzz"/></td></tr>
<tr><td>Wachtwoord:</td><td><input type="password" name="zzy"/></td></tr>
<tr><td>Domein:</td><td><select name=domain><option selected value=swmeppel>Seniorweb Meppel</option>
<p>
<tr><td colspan=2> <font size=1> Deze site maakt gebruik van cookies om het inloggen werkend te maken.<br>Verder word er absoluut niks gelogd in cookies.<p>Door in te loggen gaat u akkoord hiermee.<br>Niet dat ik het eens ben met deze wetgeving, maar het is verplicht dit te melden.</font></td></tr>
LAPTEKST

print "</select></td></tr>\n<p>\n</table>";
}; 
} else {
print "</h1>";

print $UpdatePW;

########################################################################### 
########################################################################### 

#if($mySessions =~ / reg/){ print "reg ok" } else { print "reg !ok"; };

 if($out{fn} =~ /^$/){ 
   require "a/start" or die("Structurele fout in de bestandsstructuur."); 
 } elsif(($out{fn} =~ /^00a$|^00b$/)){ 
  if($out{doc} =~ /^$/){
   require "a/$out{fn}" or die ("Fout. Controleer of je goed bent aangemeld."); 
   } else {
   require "a/docwrapper";
  };
 } else { 
  if (-e "a/$out{fn}") {
   require "a/$out{fn}" or die ("Fout. Controleer of je goed bent aangemeld."); 
  } else {
 require "a/404"
  };
 };
};

########################################################################### 
########################################################################### Schrijf laatste stuk HTML
print <<LASTHTML;
</td>
</tr>
<tr>
<td bgcolor=#CCCCCC width=1000 height=65 colspan=2 align=right>
LASTHTML


if($icanhasbutton =~ "yes"){
 print "<input type=submit $lock value=Volgende\&gt>";
};

print <<LAPTEKST; 
</form></td>
</tr>
</table>
<font size=2 color=white><i>&copy 2012-2014 Fland.re Webservices</i></font>
</body>
</html>
LAPTEKST
