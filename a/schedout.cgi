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
$Pag = $dbh->prepare("SELECT users.id, users.initials, users.mname, users.lname, users.phonehome, users.phonemobile, schedule.d11, schedule.d12, schedule.d13, schedule.d14, schedule.d15, schedule.d21, schedule.d22, schedule.d23, schedule.d24, schedule.d25, schedule.d31, schedule.d32, schedule.d33, schedule.d34, schedule.d35, schedule.d41, schedule.d42, schedule.d43, schedule.d44, schedule.d45, schedule.d51, schedule.d52, schedule.d53, schedule.d54, schedule.d55, schedule.notes, schedule.lastModified, users.swtask, users.email FROM users left join schedule on users.id = schedule.id order by users.lname asc");
$Pag->execute();

if(!$out{footer}){ $out{footer} = "Werk deze gegevens bij via <b>http://planbord.swmeppel.nl</b>"; };
if(!$out{header}){ $out{header} = "Seniorweb Meppel - Roosters"; };
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
<center><font size=$out{hdrFontSize}><b>$out{header}</b></font><br></center>
<b>Individuele roosters weergeven: <a href=./schedout.cgi?>Ja</a> | <a href=./schedout.cgi?noTotals=1>Nee</a></b>
<hr>
DURR

while (@naw = $Pag->fetchrow()) {
 $name = $naw[1]." ".$naw[2]." ".$naw[3];
if($naw[33] =~ /^ass$/){ $txlbl = "Assistent"; }; 
if($naw[33] =~ /^doc$/){ $txlbl = "Docent"; };
if($naw[33] =~ /^docass$/){ $txlbl = "Docent/assistent"; };
if($naw[33] =~ /^other$/){ $txlbl = "Iets anders"; };
 if($naw[32] =~ /^$/) { 

if(!$out{noTotals}){
print <<DERP;
<h2>Roosterbord voor $name ($txlbl)</h2>
<table width=600px>
<tr><td></td> <th width=100px>Ma</th><th width=100px>Di</th><th width=100px>Wo</th><th width=100px>Do</th><th width=100px>Vr</th></tr>
<tr><td>09:30</td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td></tr>
<tr><td>11:00</td><td bgcolor=#cccccc colspan=5 align=center><b>Geen rooster ingevuld!</b></td></tr>
<tr><td>13:15</td><td bgcolor=#cccccc colspan=5 align=center><b>Te bereiken op: $naw[4] $naw[5] </b></td></tr>
<tr><td>15:15</td><td bgcolor=#cccccc colspan=5 align=center><b>$naw[34]</b></td></tr>
<tr><td>19:00</td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td><td bgcolor=#cccccc></td></tr>
</table>
<hr>
DERP

};
 };

if($naw[32]) {
################ Select box selector (please kill me it hurts to live)
if($naw[6] =~ /1/){ $d11 = "bgcolor=green>Ja"; $e11++; $n11 = $n11.$name." (".$naw[33].") <br> "; } elsif($naw[6] =~ /2/){ $d11 = "bgcolor=yellow>Misschien"; $f11++; $m11 = $m11.$name." (".$naw[33].") <br> "; } elsif($naw[6] =~ /3/){ $d11 = "bgcolor=red>Nee"; $g11++;  $l11 = $l11.$name." (".$naw[33].") <br> ";};
if($naw[7] =~ /1/){ $d12 = "bgcolor=green>Ja"; $e12++; $n12 = $n12.$name." (".$naw[33].") <br> "; } elsif($naw[7] =~ /2/){ $d12 = "bgcolor=yellow>Misschien"; $f12++;  $m12 = $m12.$name." (".$naw[33].") <br> ";} elsif($naw[7] =~ /3/){ $d12 = "bgcolor=red>Nee"; $g12++;  $l12 = $l12.$name." (".$naw[33].") <br> ";};
if($naw[8] =~ /1/){ $d13 = "bgcolor=green>Ja"; $e13++; $n13 = $n13.$name." (".$naw[33].") <br> ";  } elsif($naw[8] =~ /2/){ $d13 = "bgcolor=yellow>Misschien"; $f13++;  $m13 = $m13.$name." (".$naw[33].") <br> ";} elsif($naw[8] =~ /3/){ $d13 = "bgcolor=red>Nee"; $g13++;  $l13 = $l13.$name." (".$naw[33].") <br> ";};
if($naw[9] =~ /1/){ $d14 = "bgcolor=green>Ja"; $e14++; $n14 = $n14.$name." (".$naw[33].") <br> ";  } elsif($naw[9] =~ /2/){ $d14 = "bgcolor=yellow>Misschien"; $f14++;  $m14 = $m14.$name." (".$naw[33].") <br> ";} elsif($naw[9] =~ /3/){ $d14 = "bgcolor=red>Nee"; $g14++;  $l14 = $l14.$name." (".$naw[33].") <br> ";};
if($naw[10] =~ /1/){ $d15 = "bgcolor=green>Ja"; $e15++; $n15 = $n15.$name." (".$naw[33].") <br> "; } elsif($naw[10] =~ /2/){ $d15 = "bgcolor=yellow>Misschien"; $f15++; $m15 = $m15.$name." (".$naw[33].") <br> ";} elsif($naw[10] =~ /3/){ $d15 = "bgcolor=red>Nee"; $g15++;  $l15 = $l15.$name." (".$naw[33].") <br> ";};
if($naw[11] =~ /1/){ $d21 = "bgcolor=green>Ja"; $e21++; $n21 = $n21.$name." (".$naw[33].") <br> "; } elsif($naw[11] =~ /2/){ $d21 = "bgcolor=yellow>Misschien"; $f21++; $m21 = $m21.$name." (".$naw[33].") <br> ";} elsif($naw[11] =~ /3/){ $d21 = "bgcolor=red>Nee"; $g21++;  $l21 = $l21.$name." (".$naw[33].") <br> ";};
if($naw[12] =~ /1/){ $d22 = "bgcolor=green>Ja"; $e22++; $n22 = $n22.$name." (".$naw[33].") <br> "; } elsif($naw[12] =~ /2/){ $d22 = "bgcolor=yellow>Misschien"; $f22++; $m22 = $m22.$name." (".$naw[33].") <br> ";} elsif($naw[12] =~ /3/){ $d22 = "bgcolor=red>Nee"; $g22++;  $l22 = $l22.$name." (".$naw[33].") <br> ";};
if($naw[13] =~ /1/){ $d23 = "bgcolor=green>Ja"; $e23++; $n23 = $n23.$name." (".$naw[33].") <br> "; } elsif($naw[13] =~ /2/){ $d23 = "bgcolor=yellow>Misschien"; $f23++; $m23 = $m23.$name." (".$naw[33].") <br> ";} elsif($naw[13] =~ /3/){ $d23 = "bgcolor=red>Nee"; $g23++;  $l23 = $l23.$name." (".$naw[33].") <br> ";};
if($naw[14] =~ /1/){ $d24 = "bgcolor=green>Ja"; $e24++; $n24 = $n24.$name." (".$naw[33].") <br> "; } elsif($naw[14] =~ /2/){ $d24 = "bgcolor=yellow>Misschien"; $f24++; $m24 = $m24.$name." (".$naw[33].") <br> ";} elsif($naw[14] =~ /3/){ $d24 = "bgcolor=red>Nee"; $g24++;  $l24 = $l24.$name." (".$naw[33].") <br> ";};
if($naw[15] =~ /1/){ $d25 = "bgcolor=green>Ja"; $e25++; $n25 = $n25.$name." (".$naw[33].") <br> "; } elsif($naw[15] =~ /2/){ $d25 = "bgcolor=yellow>Misschien"; $f25++; $m25 = $m25.$name." (".$naw[33].") <br> ";} elsif($naw[15] =~ /3/){ $d25 = "bgcolor=red>Nee"; $g25++;  $l25 = $l25.$name." (".$naw[33].") <br> ";};
if($naw[16] =~ /1/){ $d31 = "bgcolor=green>Ja"; $e31++; $n31 = $n31.$name." (".$naw[33].") <br> "; } elsif($naw[16] =~ /2/){ $d31 = "bgcolor=yellow>Misschien"; $f31++; $m31 = $m31.$name." (".$naw[33].") <br> ";} elsif($naw[16] =~ /3/){ $d31 = "bgcolor=red>Nee"; $g31++;  $l31 = $l31.$name." (".$naw[33].") <br> ";};
if($naw[17] =~ /1/){ $d32 = "bgcolor=green>Ja"; $e32++; $n32 = $n32.$name." (".$naw[33].") <br> "; } elsif($naw[17] =~ /2/){ $d32 = "bgcolor=yellow>Misschien"; $f32++; $m32 = $m32.$name." (".$naw[33].") <br> ";} elsif($naw[17] =~ /3/){ $d32 = "bgcolor=red>Nee"; $g32++;  $l32 = $l32.$name." (".$naw[33].") <br> ";};
if($naw[18] =~ /1/){ $d33 = "bgcolor=green>Ja"; $e33++; $n33 = $n33.$name." (".$naw[33].") <br> "; } elsif($naw[18] =~ /2/){ $d33 = "bgcolor=yellow>Misschien"; $f33++; $m33 = $m33.$name." (".$naw[33].") <br> ";} elsif($naw[18] =~ /3/){ $d33 = "bgcolor=red>Nee"; $g33++;  $l33 = $l33.$name." (".$naw[33].") <br> ";};
if($naw[19] =~ /1/){ $d34 = "bgcolor=green>Ja"; $e34++; $n34 = $n34.$name." (".$naw[33].") <br> "; } elsif($naw[19] =~ /2/){ $d34 = "bgcolor=yellow>Misschien"; $f34++; $m34 = $m34.$name." (".$naw[33].") <br> ";} elsif($naw[19] =~ /3/){ $d34 = "bgcolor=red>Nee"; $g34++;  $l34 = $l34.$name." (".$naw[33].") <br> ";};
if($naw[20] =~ /1/){ $d35 = "bgcolor=green>Ja"; $e35++; $n35 = $n35.$name." (".$naw[33].") <br> "; } elsif($naw[20] =~ /2/){ $d35 = "bgcolor=yellow>Misschien"; $f35++; $m35 = $m35.$name." (".$naw[33].") <br> ";} elsif($naw[20] =~ /3/){ $d35 = "bgcolor=red>Nee"; $g35++;  $l35 = $l35.$name." (".$naw[33].") <br> ";};
if($naw[21] =~ /1/){ $d41 = "bgcolor=green>Ja"; $e41++; $n41 = $n41.$name." (".$naw[33].") <br> "; } elsif($naw[21] =~ /2/){ $d41 = "bgcolor=yellow>Misschien"; $f41++; $m41 = $m41.$name." (".$naw[33].") <br> ";} elsif($naw[21] =~ /3/){ $d41 = "bgcolor=red>Nee"; $g41++;  $l41 = $l41.$name." (".$naw[33].") <br> ";};
if($naw[22] =~ /1/){ $d42 = "bgcolor=green>Ja"; $e42++; $n42 = $n42.$name." (".$naw[33].") <br> "; } elsif($naw[22] =~ /2/){ $d42 = "bgcolor=yellow>Misschien"; $f42++; $m42 = $m42.$name." (".$naw[33].") <br> ";} elsif($naw[22] =~ /3/){ $d42 = "bgcolor=red>Nee"; $g42++;  $l42 = $l42.$name." (".$naw[33].") <br> ";};
if($naw[23] =~ /1/){ $d43 = "bgcolor=green>Ja"; $e43++; $n43 = $n43.$name." (".$naw[33].") <br> "; } elsif($naw[23] =~ /2/){ $d43 = "bgcolor=yellow>Misschien"; $f43++; $m43 = $m43.$name." (".$naw[33].") <br> ";} elsif($naw[23] =~ /3/){ $d43 = "bgcolor=red>Nee"; $g43++;  $l43 = $l43.$name." (".$naw[33].") <br> ";};
if($naw[24] =~ /1/){ $d44 = "bgcolor=green>Ja"; $e44++; $n44 = $n44.$name." (".$naw[33].") <br> "; } elsif($naw[24] =~ /2/){ $d44 = "bgcolor=yellow>Misschien"; $f44++; $m44 = $m44.$name." (".$naw[33].") <br> ";} elsif($naw[24] =~ /3/){ $d44 = "bgcolor=red>Nee"; $g44++;  $l44 = $l44.$name." (".$naw[33].") <br> ";};
if($naw[25] =~ /1/){ $d45 = "bgcolor=green>Ja"; $e45++; $n45 = $n45.$name." (".$naw[33].") <br> "; } elsif($naw[25] =~ /2/){ $d45 = "bgcolor=yellow>Misschien"; $f45++; $m45 = $m45.$name." (".$naw[33].") <br> ";} elsif($naw[25] =~ /3/){ $d45 = "bgcolor=red>Nee"; $g45++;  $l45 = $l45.$name." (".$naw[33].") <br> ";};
if($naw[26] =~ /1/){ $d51 = "bgcolor=green>Ja"; $e51++; $n51 = $n51.$name." (".$naw[33].") <br> "; } elsif($naw[26] =~ /2/){ $d51 = "bgcolor=yellow>Misschien"; $f51++; $m51 = $m51.$name." (".$naw[33].") <br> ";} elsif($naw[26] =~ /3/){ $d51 = "bgcolor=red>Nee"; $g51++;  $l51 = $l51.$name." (".$naw[33].") <br> ";};
if($naw[27] =~ /1/){ $d52 = "bgcolor=green>Ja"; $e52++; $n52 = $n52.$name." (".$naw[33].") <br> "; } elsif($naw[27] =~ /2/){ $d52 = "bgcolor=yellow>Misschien"; $f52++; $m52 = $m52.$name." (".$naw[33].") <br> ";} elsif($naw[27] =~ /3/){ $d52 = "bgcolor=red>Nee"; $g52++;  $l52 = $l52.$name." (".$naw[33].") <br> ";};
if($naw[28] =~ /1/){ $d53 = "bgcolor=green>Ja"; $e53++; $n53 = $n53.$name." (".$naw[33].") <br> "; } elsif($naw[28] =~ /2/){ $d53 = "bgcolor=yellow>Misschien"; $f53++; $m53 = $m53.$name." (".$naw[33].") <br> ";} elsif($naw[28] =~ /3/){ $d53 = "bgcolor=red>Nee"; $g53++;  $l53 = $l53.$name." (".$naw[33].") <br> ";};
if($naw[29] =~ /1/){ $d54 = "bgcolor=green>Ja"; $e54++; $n54 = $n54.$name." (".$naw[33].") <br> "; } elsif($naw[29] =~ /2/){ $d54 = "bgcolor=yellow>Misschien"; $f54++; $m54 = $m54.$name." (".$naw[33].") <br> ";} elsif($naw[29] =~ /3/){ $d54 = "bgcolor=red>Nee"; $g54++;  $l54 = $l54.$name." (".$naw[33].") <br> ";};
if($naw[30] =~ /1/){ $d55 = "bgcolor=green>Ja"; $e55++; $n55 = $n55.$name." (".$naw[33].") <br> "; } elsif($naw[30] =~ /2/){ $d55 = "bgcolor=yellow>Misschien"; $f55++; $m55 = $m55.$name." (".$naw[33].") <br> ";} elsif($naw[30] =~ /3/){ $d55 = "bgcolor=red>Nee"; $g55++;  $l55 = $l55.$name." (".$naw[33].") <br> ";};

if(!$out{noTotals}){
print <<DERP;
<h2>Roosterbord voor $name ($txlbl)</h2>
<table width=600px>
<tr><td></td> <th width=100px>Ma</th><th width=100px>Di</th><th width=100px>Wo</th><th width=100px>Do</th><th width=100px>Vr</th></tr>
<tr><td>09:30</td><td $d11</td><td $d21</td><td $d31</td><td $d41</td><td $d51</td></tr>
<tr><td>11:00</td><td $d12</td><td $d22</td><td $d32</td><td $d42</td><td $d52</td></tr>
<tr><td>13:15</td><td $d13</td><td $d23</td><td $d33</td><td $d43</td><td $d53</td></tr>
<tr><td>15:15</td><td $d14</td><td $d24</td><td $d34</td><td $d44</td><td $d54</td></tr>
<tr><td>19:00</td><td $d15</td><td $d25</td><td $d35</td><td $d45</td><td $d55</td></tr>
</table>
<p>
<b>Notities:</b><br>
$naw[31]
<p>
<i>Dit rooster is voor het laatst bewerkt op $naw[32]</i>
</table>
<hr>
DERP

};

};
};

print <<DURR;
<hr>
<h2>Totaalcijfers van alle roosters</h2>
<b>Individuele roosters weergeven: <a href=./schedout.cgi?>Ja</a> | <a href=./schedout.cgi?noTotals=1>Nee</a></b>
<p>
<table width=600px>
<tr><td></td> <th width=100px colspan=3>Ma</th><th width=100px colspan=3>Di</th><th width=100px colspan=3>Wo</th><th width=100px colspan=3>Do</th><th width=100px colspan=3>Vr</th></tr>
<tr><td>09:30</td><td bgcolor=#ccff99>$e11</td><td bgcolor=#ffff99>$f11</td><td bgcolor=#ff6633>$g11</td><td bgcolor=#ccff99>$e21<td bgcolor=#ffff99>$f21</td><td bgcolor=#ff6633>$g21</td><td bgcolor=#ccff99>$e31</td><td bgcolor=#ffff99>$f31</td><td bgcolor=#ff6633>$g31</td><td bgcolor=#ccff99>$e41</td><td bgcolor=#ffff99>$f41</td><td bgcolor=#ff6633>$g41</td><td bgcolor=#ccff99>$e51</td><td bgcolor=#ffff99>$f51</td><td bgcolor=#ff6633>$g51</td></tr>
<tr><td>11:00</td><td bgcolor=#ccff99>$e12</td><td bgcolor=#ffff99>$f12</td><td bgcolor=#ff6633>$g12</td><td bgcolor=#ccff99>$e22<td bgcolor=#ffff99>$f22</td><td bgcolor=#ff6633>$g22</td><td bgcolor=#ccff99>$e32</td><td bgcolor=#ffff99>$f32</td><td bgcolor=#ff6633>$g32</td><td bgcolor=#ccff99>$e42</td><td bgcolor=#ffff99>$f42</td><td bgcolor=#ff6633>$g42</td><td bgcolor=#ccff99>$e52</td><td bgcolor=#ffff99>$f52</td><td bgcolor=#ff6633>$g52</td></tr>
<tr><td>13:15</td><td bgcolor=#ccff99>$e13</td><td bgcolor=#ffff99>$f13</td><td bgcolor=#ff6633>$g13</td><td bgcolor=#ccff99>$e23<td bgcolor=#ffff99>$f23</td><td bgcolor=#ff6633>$g23</td><td bgcolor=#ccff99>$e33</td><td bgcolor=#ffff99>$f33</td><td bgcolor=#ff6633>$g33</td><td bgcolor=#ccff99>$e43</td><td bgcolor=#ffff99>$f43</td><td bgcolor=#ff6633>$g43</td><td bgcolor=#ccff99>$e53</td><td bgcolor=#ffff99>$f53</td><td bgcolor=#ff6633>$g53</td></tr>
<tr><td>15:15</td><td bgcolor=#ccff99>$e14</td><td bgcolor=#ffff99>$f14</td><td bgcolor=#ff6633>$g14</td><td bgcolor=#ccff99>$e24<td bgcolor=#ffff99>$f24</td><td bgcolor=#ff6633>$g24</td><td bgcolor=#ccff99>$e34</td><td bgcolor=#ffff99>$f34</td><td bgcolor=#ff6633>$g34</td><td bgcolor=#ccff99>$e44</td><td bgcolor=#ffff99>$f44</td><td bgcolor=#ff6633>$g44</td><td bgcolor=#ccff99>$e54</td><td bgcolor=#ffff99>$f54</td><td bgcolor=#ff6633>$g54</td></tr>
<tr><td>19:00</td><td bgcolor=#ccff99>$e15</td><td bgcolor=#ffff99>$f15</td><td bgcolor=#ff6633>$g15</td><td bgcolor=#ccff99>$e25<td bgcolor=#ffff99>$f25</td><td bgcolor=#ff6633>$g25</td><td bgcolor=#ccff99>$e35</td><td bgcolor=#ffff99>$f35</td><td bgcolor=#ff6633>$g35</td><td bgcolor=#ccff99>$e45</td><td bgcolor=#ffff99>$f45</td><td bgcolor=#ff6633>$g45</td><td bgcolor=#ccff99>$e55</td><td bgcolor=#ffff99>$f55</td><td bgcolor=#ff6633>$g55</td></tr>
</table>
<p>
<table  width=600px>
<tr><th colspan=6>Maandag</th></tr>
<tr><th></th><th>Ja</th><th>Misschien</th><th>Nee</th>
<tr><td>09:30</td><td valign=top bgcolor=#ccff99>$n11</td><td valign=top bgcolor=#ffff99>$m11</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>11:00</td><td valign=top bgcolor=#ccff99>$n12</td><td valign=top bgcolor=#ffff99>$m12</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>13:15</td><td valign=top bgcolor=#ccff99>$n13</td><td valign=top bgcolor=#ffff99>$m13</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>15:15</td><td valign=top bgcolor=#ccff99>$n14</td><td valign=top bgcolor=#ffff99>$m14</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>19:00</td><td valign=top bgcolor=#ccff99>$n15</td><td valign=top bgcolor=#ffff99>$m15</td><td valign=top bgcolor=#ff6633></td></tr>
</table>
<p>
<table width=600px>
<tr><th colspan=6>Dinsdag</th></tr>
<tr><th></th><th>Ja</th><th>Misschien</th><th>Nee</th>
<tr><td>09:30</td><td valign=top bgcolor=#ccff99>$n21</td><td valign=top bgcolor=#ffff99>$m21</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>11:00</td><td valign=top bgcolor=#ccff99>$n22</td><td valign=top bgcolor=#ffff99>$m22</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>13:15</td><td valign=top bgcolor=#ccff99>$n23</td><td valign=top bgcolor=#ffff99>$m23</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>15:15</td><td valign=top bgcolor=#ccff99>$n24</td><td valign=top bgcolor=#ffff99>$m24</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>19:00</td><td valign=top bgcolor=#ccff99>$n25</td><td valign=top bgcolor=#ffff99>$m25</td><td valign=top bgcolor=#ff6633></td></tr>
</table>
<p>
<table width=600px>
<tr><th colspan=6>Woensdag</th></tr>
<tr><th></th><th>Ja</th><th>Misschien</th><th>Nee</th>
<tr><td>09:30</td><td valign=top bgcolor=#ccff99>$n31</td><td valign=top bgcolor=#ffff99>$m31</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>11:00</td><td valign=top bgcolor=#ccff99>$n32</td><td valign=top bgcolor=#ffff99>$m32</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>13:15</td><td valign=top bgcolor=#ccff99>$n33</td><td valign=top bgcolor=#ffff99>$m33</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>15:15</td><td valign=top bgcolor=#ccff99>$n34</td><td valign=top bgcolor=#ffff99>$m34</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>19:00</td><td valign=top bgcolor=#ccff99>$n35</td><td valign=top bgcolor=#ffff99>$m35</td><td valign=top bgcolor=#ff6633></td></tr>
</table>
<p>
<table width=600px>
<tr><th colspan=6>Donderdag</th></tr>
<tr><th></th><th>Ja</th><th>Misschien</th><th>Nee</th>
<tr><td>09:30</td><td valign=top bgcolor=#ccff99>$n41</td><td valign=top bgcolor=#ffff99>$m41</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>11:00</td><td valign=top bgcolor=#ccff99>$n42</td><td valign=top bgcolor=#ffff99>$m42</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>13:15</td><td valign=top bgcolor=#ccff99>$n43</td><td valign=top bgcolor=#ffff99>$m43</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>15:15</td><td valign=top bgcolor=#ccff99>$n44</td><td valign=top bgcolor=#ffff99>$m44</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>19:00</td><td valign=top bgcolor=#ccff99>$n45</td><td valign=top bgcolor=#ffff99>$m45</td><td valign=top bgcolor=#ff6633></td></tr>
</table>
<p>
<table width=600px>
<tr><th colspan=6>Vrijdag</th></tr>
<tr><th></th><th>Ja</th><th>Misschien</th><th>Nee</th>
<tr><td>09:30</td><td valign=top bgcolor=#ccff99>$n51</td><td valign=top bgcolor=#ffff99>$m51</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>11:00</td><td valign=top bgcolor=#ccff99>$n52</td><td valign=top bgcolor=#ffff99>$m52</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>13:15</td><td valign=top bgcolor=#ccff99>$n53</td><td valign=top bgcolor=#ffff99>$m53</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>15:15</td><td valign=top bgcolor=#ccff99>$n54</td><td valign=top bgcolor=#ffff99>$m54</td><td valign=top bgcolor=#ff6633></td></tr>
<tr><td>19:00</td><td valign=top bgcolor=#ccff99>$n55</td><td valign=top bgcolor=#ffff99>$m55</td><td valign=top bgcolor=#ff6633></td></tr>
</table>
</body>
</html>
DURR


