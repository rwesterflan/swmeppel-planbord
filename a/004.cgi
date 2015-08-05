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

$session = CGI::Session->load() or die CGI::Session->errstr();
$CGISESSION = $session->id();
if(!$CGISESSION) { print "<script type=text/javascript>  window.location.href = \"../\";</script> "; exit; };
$domain = $session->param('domain');
print $domain." service.";

print $out{request};
require "dbd.cfg"; 
 
########################################################################### 02n
if($out{request} =~ /^02n$/){
$dbh->do("DELETE FROM users WHERE id=$out{doMe};");
$targetURL="00n";
};

########################################################################### 01j
if($out{request} =~ /^01j$/){
if($out{doMe} =~ /new/){
$dbh->do("INSERT INTO distribution VALUES ('', '$out{name}', '$out{address1}', '$out{address2}', '$out{postal}', '$out{city}', '$out{phone1}', '$out{phone2}', '$out{email}', '$out{contact}', '$out{amount}', '$out{distributor}', '$out{notes}')");
} else {
$dbh->do("UPDATE distribution SET name='$out{name}', address1='$out{address1}', address2='$out{address2}', postal='$out{postal}', city='$out{city}', phone1='$out{phone1}', phone2='$out{phone2}', email='$out{email}', contact='$out{contact}', amount='$out{amount}', distributor='$out{distributor}', notes='$out{notes}' WHERE id='$out{doMe}';") or die(mysql_error()); ;
};
$targetURL="00j";
};

########################################################################### 02n
if($out{request} =~ /^00o$/){
$pwd = sha1_hex("$out{pass}_$out{user}");
$dbh->do("INSERT INTO users VALUES ('', '$out{displayname}', '$out{user}', '$pwd', '$out{isAdmin}', '$isEmployee', '$isGuest', '1', 'X')");
$targetURL="00n";
};

########################################################################### 01n
if($out{request} =~ /^01n$/){

if($out{updateBrowser} =~ /on/){ 
$uip = $ENV{'REMOTE_ADDR'};
$ubrowser = $ENV{'HTTP_USER_AGENT'};
} else {
$ubrowser = $out{oldbrowser};
$uip = $out{oldip};
};

$ubrowser =~ s/\'//g; 

 if($out{resetPW} =~ /on/){ 
  $pwd = sha1_hex("$out{password}_$out{altusername}");
  $dbh->do("UPDATE users SET title='$out{title}', initials='$out{initials}', fname='$out{fname}', mname='$out{mname}', lname='$out{lname}', street='$out{street}', postal='$out{postal}', city='$out{city}', phonehome='$out{phonehome}', phonemobile='$out{phonemobile}', email='$out{email}', task='$out{task}', swtask='$out{swtask}', birthday='$out{birthday}', membersince='$out{membersince}', elevation='$out{elevation}', ip='$uip', browser='$ubrowser', password='$pwd', hardware='$out{hardware}' WHERE id='$out{id}';") or die(mysql_error()); ;
 } else {
  $dbh->do("UPDATE users SET title='$out{title}', initials='$out{initials}', fname='$out{fname}', mname='$out{mname}', lname='$out{lname}', street='$out{street}', postal='$out{postal}', city='$out{city}', phonehome='$out{phonehome}', phonemobile='$out{phonemobile}', email='$out{email}', task='$out{task}', swtask='$out{swtask}', birthday='$out{birthday}', membersince='$out{membersince}', elevation='$out{elevation}', ip='$uip', browser='$ubrowser', hardware='$out{hardware}' WHERE id='$out{id}';") or die(mysql_error()); ;
 };
$targetURL="00n";
};

########################################################################### 00r
if($out{request} =~ /^00r$/){

if($out{newPass1} =~ /$out{newPass2}/){
  $pwd = sha1_hex("$out{newPass1}_$out{altusername}");
  $dbh->do("UPDATE users SET password='$pwd' WHERE id='$out{id}';") or die(mysql_error()); ;
$targetURL="00r&status=ok";

 } else {
$targetURL="00r&status=failed&reason=DoesNotMatch";
 };
};

########################################################################### 00g
if($out{request} =~ /^00g$/){
$str = $buffer;
$dbh->do("UPDATE users SET courses='$str' WHERE id='$out{doMe}';") or die(mysql_error()); ;
$targetURL="00g&success=1&doMe=$out{doMe}";
};

########################################################################### 00b
if($out{request} =~ /^00b$/){

if(($out{c1} =~ /^$/) && ($out{c2} =~ /^$/) && ($out{c3} =~ /^$/)){
$targetURL="00b&warning=2&menu=off";
} else {

$uip = $ENV{'REMOTE_ADDR'};
$ubrowser = $ENV{'HTTP_USER_AGENT'};
$dbh->do("INSERT INTO enq VALUES ('', '$out{courseID}', '$out{courseDate}', '$out{courseRef}', '$out{courseRefOther}', '$out{c1}', '$out{c2}', '$out{c3}', '$out{c4}', '$out{c5}', '$out{c6}', '$out{c7}', '$out{courseSuggestions}', '$out{courseContact}', '$out{courseIdeas}', '$out{courseEmail}', '$out{courseKeepMePosted}', '$ubrowser', '$uip')");
if($out{enq} =~ /1/){
$targetURL="00b&warning=1&menu=off";
} else {
$targetURL="00b&warning=1";
};
};
};

########################################################################### 00c
if($out{request} =~ /^00c$/){
$dbh->do("UPDATE coursesched SET courseid='$out{d11a}' where day='d11a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d11b}' where day='d11b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d12a}' where day='d12a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d12b}' where day='d12b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d13a}' where day='d13a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d13b}' where day='d13b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d14a}' where day='d14a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d14b}' where day='d14b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d15a}' where day='d15a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d15b}' where day='d15b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d21a}' where day='d21a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d21b}' where day='d21b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d22a}' where day='d22a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d22b}' where day='d22b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d23a}' where day='d23a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d23b}' where day='d23b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d24a}' where day='d24a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d24b}' where day='d24b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d25a}' where day='d25a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d25b}' where day='d25b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d31a}' where day='d31a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d31b}' where day='d31b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d32a}' where day='d32a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d32b}' where day='d32b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d33a}' where day='d33a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d33b}' where day='d33b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d34a}' where day='d34a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d34b}' where day='d34b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d35a}' where day='d35a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d35b}' where day='d35b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d41a}' where day='d41a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d41b}' where day='d41b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d42a}' where day='d42a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d42b}' where day='d42b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d43a}' where day='d43a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d43b}' where day='d43b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d44a}' where day='d44a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d44b}' where day='d44b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d45a}' where day='d45a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d45b}' where day='d45b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d51a}' where day='d51a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d51b}' where day='d51b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d52a}' where day='d52a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d52b}' where day='d52b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d53a}' where day='d53a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d53b}' where day='d53b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d54a}' where day='d54a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d54b}' where day='d54b';");
$dbh->do("UPDATE coursesched SET courseid='$out{d55a}' where day='d55a';");
$dbh->do("UPDATE coursesched SET courseid='$out{d55b}' where day='d55b';");

$targetURL="00m";
};

########################################################################### 01e
if($out{request} =~ /^01e$/){
$dbh->do("UPDATE schedule SET d11='$out{d11}', d12='$out{d12}', d13='$out{d13}', d14='$out{d14}', d15='$out{d15}', d21='$out{d21}', d22='$out{d22}', d23='$out{d23}', d24='$out{d24}', d25='$out{d25}', d31='$out{d31}', d32='$out{d32}', d33='$out{d33}', d34='$out{d34}', d35='$out{d35}', d41='$out{d41}', d42='$out{d42}', d43='$out{d43}', d44='$out{d44}', d45='$out{d45}', d51='$out{d51}', d52='$out{d52}', d53='$out{d53}', d54='$out{d54}', d55='$out{d55}', notes='$out{notes}', lastModified='$out{datum}, $out{tijd}' WHERE id='$out{id}';") or die(mysql_error()); ;
$targetURL="00f";
};

########################################################################### 00y
if($out{request} =~ /^00y$/){
$dbh->do("UPDATE config SET value='$out{companyname}' WHERE naam='companyname';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{companybtw}' WHERE naam='companybtw';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{companykvk}' WHERE naam='companykvk';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{companybank}' WHERE naam='companybank';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{companycall}' WHERE naam='companycall';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{maintitle}' WHERE naam='maintitle';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{footer}' WHERE naam='footer';") or die(mysql_error()); ;
$dbh->do("UPDATE config SET value='$out{license}' WHERE naam='license';") or die(mysql_error()); ;

$targetURL="00y";
};

########################################################################### 01w
if($out{request} =~ /^00w$/){

if($out{message} =~ /^$/){
print "Leeg bericht -- doorsturen...";
$targetURL="00w&warning=emptyMessage";
} else {
$out{message} =~ s/\</\&lt;/g; 
$out{message} =~ s/\>/\&gt;/g; 

if($out{flagOn} =~ /on/){ } else { $out{isFlagged} = "0"; };
if($out{isFlagged} =~ /test/){ $testflag = "[TEST]"};
if($out{isFlagged} =~ /belangrijk/){ $testflag = "[LET OP]"};
if($out{isFlagged} =~ /update/){ $testflag = "[UPDATE]"};
$uip = $ENV{'REMOTE_ADDR'};
$ubrowser = $ENV{'HTTP_USER_AGENT'};
$dbh->do("INSERT INTO sms VALUES ('', '$out{date}', '$out{time}', '$out{byUser}', '$testflag $out{message}', '$out{isFlagged}', '$uip', '$ubrowser');");
$targetURL="00w";
};

};

########################################################################### 02w
if($out{request} =~ /^02w$/){
$dbh->do("DELETE FROM sms WHERE id=$out{doMe};");
$targetURL="00w";
};

########################################################################### 02j
if($out{request} =~ /^02j$/){
$dbh->do("DELETE FROM distribution WHERE id=$out{doMe};");
$targetURL="00j";
};


########################################################################### 01s
if($out{request} =~ /^01s$/){
 if($out{doMe}){
$dbh->do("UPDATE address SET title='$out{title}', name='$out{name}', street='$out{street}', postalcity='$out{postalcity}', phonenr='$out{phonenr}', mobilenr='$out{mobilenr}', email='$out{email}', company='$out{company}', companystreet='$out{companystreet}', companypostalcity='$out{companypostalcity}', companyphonenr='$out{companyphonenr}', companymobilenr='$out{companymobilenr}', companyfax='$out{companyfax}', companywebsite='$out{companywebsite}', notes='$out{notes}', distance='$out{distance}' WHERE id='$out{doMe}'");
} else {
$dbh->do("INSERT INTO address VALUES ('', '$out{title}', '$out{name}', '$out{street}', '$out{postalcity}', '$out{phonenr}', '$out{mobilenr}', '$out{email}', '$out{company}', '$out{companystreet}', '$out{companypostalcity}', '$out{companyphonenr}', '$out{companymobilenr}', '$out{companyfax}', '$out{companywebsite}', '$out{notes}', '$out{distance}');");
};

$targetURL="00s";
};

########################################################################### 02s
if($out{request} =~ /^02s$/){
$dbh->do("DELETE FROM address WHERE id=$out{doMe};");
$targetURL="00s";
};

########################################################################### 05e
if($out{request} =~ /^05e$/){
$dbh->do("insert into schedule values ('$out{id}', 'Hier kan extra uitleg geplaatst worden...', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3' ,'3' ,'3', '$out{datum}, $out{tijd}', '$out{datum}, $out{tijd}')");
$targetURL="00e";
};

########################################################################### Finishing touch
print "<script type=\"text/javascript\">  window.location.href = \"../admin.cgi?fn=$targetURL\";</script>";
print "Klik <a href=../?fn=$targetURL>hier</a> als je niet word doorverwezen...";
