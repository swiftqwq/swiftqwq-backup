#!/usr/local/bin/perl
# cgi-bin/CustGen.cgi

use CGI qw(:standard);

print header;

$JSCRIPT=<<END;
function checkFields() {
	var num = document.form1.elements.length
	var validFlag = true
	for (var i=0; i<num; i++) {
		if (	(document.form1.elements[i].value == null ||
			 document.form1.elements[i].value == '' ) &&
			(typeof document.form1.elements[i] != 'submit' ||
			 typeof document.form1.elements[i] != 'reset'	)) {
			validFlag = false
			alert('The ' + document.form1.elements[i].name + ' field is blank, please enter a value.')
			document.form1.elements[i].focus()
			break
		}	
	}
	return validFlag
}
END

print start_html(
	-TITLE => "User Customisable SVG CGI Demo",
	-BGCOLOR => "navy",
	-TEXT => "white",
	-SCRIPT => $JSCRIPT
);

print "\n<FONT SIZE=\"3\" FACE=\"Helvetica\"><B><CENTER>";

print h2("User Customisable Demo");

print "Please fill in the text boxes<BR>";

print "\n<FONT COLOR=\"red\">";

print strong("N.B. Invalid input could cause failure of CGI execution");

print "\n</FONT>";

my $mode = param("hidden_mode");

if (!($mode =~ /\btrue\b/)) { 

print hr, start_form(-NAME => 'form1', -ACTION => "http://www.cs.nott.ac.uk/SVG-cgi/CustGen.cgi", -ONSUBMIT => "return checkFields()");

print hidden(-name=>'hidden_mode',-default=>["true"]);

print table(
	{-border=>undef},
        Tr(td(b("Number of rectangles: ")), td(textfield("rects", "5", 10, 10))),
	Tr(td(b("Number of circles: ")), td(textfield("circles", "5", 10, 10))),
	Tr(td(b("Number of ellipses: ")), td(textfield("ellipses", "5", 10, 10))),
	Tr(td(b("Number of lines: ")), td(textfield("lines", "10", 10, 10))),
	Tr(td(b("Number of text strings: ")), td(textfield("texts", "1", 10, 10)))
);

} else {

print hr, start_form(-NAME => 'form1', -ACTION => "http://www.cs.nott.ac.uk/SVG-cgi/Cust.cgi", -ONSUBMIT => "return checkFields()");

my $rects = param("rects");
my $circles = param("circles");
my $ellipses = param("ellipses");
my $lines = param("lines");
my $texts = param("texts");

print hidden(-name=>'hidden_rects',-default=>[$rects]);
print "\n";
print hidden(-name=>'hidden_circles',-default=>[$circles]);
print "\n";
print hidden(-name=>'hidden_ellipses',-default=>[$ellipses]);
print "\n";
print hidden(-name=>'hidden_lines',-default=>[$lines]);
print "\n";
print hidden(-name=>'hidden_texts',-default=>[$texts]);
print "\n";

print table(
	{-border=>undef},
        Tr(td(b("Viewbox x1 co-ordinate: ")), td(textfield("viewbox_x1", "0", 10, 10)), td(b("Viewbox y1 co-ordinate: ")), td(textfield("viewbox_y1", "0", 10, 10))),
	Tr(td(b("Viewbox x2 co-ordinate: ")), td(textfield("viewbox_x2", "500", 10, 10)), td(b("Viewbox y2 co-ordinate: ")), td(textfield("viewbox_y2", "500", 10, 10))),
	Tr(td(b("Svg x co-ordinate: ")), td(textfield("svg_x", "500", 10, 10)),	td(b("Svg y co-ordinate: ")), td(textfield("svg_y", "500", 10, 10))),
	Tr(td(b("Svg width: ")), td(textfield("svg_width", "500", 10, 10)), td(b("Svg height: ")), td(textfield("svg_height", "500", 10, 10))),
	Tr(td(b("Background x: ")), td(textfield("bg_x", "0", 10, 10)), td(b("Backgound y: ")), td(textfield("bg_y", "0", 10, 10))),
	Tr(td(b("Background width: ")), td(textfield("bg_width", "500", 10, 10)), td(b("Background height: ")), td(textfield("bg_height", "500", 10, 10))),
	Tr(td(b("Background fill: ")), td(textfield("bg_fill", "cyan", 10, 10)), td(b("Background stroke: ")), td(textfield("bg_stroke", "cyan", 10, 10)))
);

print p;

my @cols = qw( black silver gray white maroon red purple fuchsia green lime olive yellow navy blue teal aqua );
my $col;

print "<table border>";

for (my $i=0; $i<$rects; $i++) {

	print "<TR><TD><B>Rectangle ".($i+1)." x: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_x' VALUE='".($i*100)."' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Rectangle ".($i+1)." y: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_y' VALUE='".($i*100)."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	print "<TR><TD><B>Rectangle ".($i+1)." width: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_width' VALUE='100' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Rectangle ".($i+1)." height: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_height' VALUE='100' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	$col = int(rand @cols-1);
	print "<TR><TD><B>Rectangle ".($i+1)." fill: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_fill' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD>\n";
	$col = int(rand @cols-1);
	print "<TD><B>Rectangle ".($i+1)." stroke: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='rect".($i+1)."_stroke' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

}

print "</table>";

print p;

print "<table border>";

for (my $i=0; $i<$circles; $i++) {

	print "<TR><TD><B>Circle ".($i+1)." cx: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_cx' VALUE='".($i*100+50)."' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Circle ".($i+1)." cy: </B></TD>\n";
	if ($i <= $circles/2) { print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_cy' VALUE='".(200-$i*40)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }
	else { print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_cy' VALUE='".(200-($circles-1-$i)*40)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }	

	$col = int(rand @cols-1);
	print "<TR><TD><B>Circle ".($i+1)." fill: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_fill' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD>\n";
	$col = int(rand @cols-1);
	print "<TD><B>Circle ".($i+1)." stroke: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_stroke' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	print "<TR><TD><B>Circle ".($i+1)." r: </B></TD>\n";
	if ($i <= $circles/2) { print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_r' VALUE='".($i*10+50)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }
	else { print "<TD><INPUT TYPE='text' NAME='circle".($i+1)."_r' VALUE='".(($circles-1-$i)*10+50)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }

}

print "</table>";

print p;

print "<table border>";

for (my $i=0; $i<$ellipses; $i++) {

	print "<TR><TD><B>Ellipse ".($i+1)." cx: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_cx' VALUE='".($i*100+50)."' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Ellipse ".($i+1)." cy: </B></TD>\n";
	if ($i <= $ellipses/2) { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_cy' VALUE='".($i*40+300)."' SIZE=10 MAXLENGTH=10></TD></TR>\n"}
	else { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_cy' VALUE='".(($ellipses-1-$i)*40+300)."' SIZE=10 MAXLENGTH=10></TD></TR>\n"}

	print "<TR><TD><B>Ellipse ".($i+1)." rx: </B></TD>\n";
	if ($i <= $ellipses/2) { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_rx' VALUE='".($i*10+50)."' SIZE=10 MAXLENGTH=10></TD>\n" }
	else { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_rx' VALUE='".(($ellipses-1-$i)*10+50)."' SIZE=10 MAXLENGTH=10></TD>\n" }
	print "<TD><B>Ellipse ".($i+1)." ry: </B></TD>\n";
	if ($i <= $ellipses/2) { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_ry' VALUE='".($i*5+20)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }
	else { print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_ry' VALUE='".(($ellipses-1-$i)*5+20)."' SIZE=10 MAXLENGTH=10></TD></TR>\n" }

	$col = int(rand @cols-1);
	print "<TR><TD><B>Ellipse ".($i+1)." fill: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_fill' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD>\n";
	$col = int(rand @cols-1);
	print "<TD><B>Ellipse ".($i+1)." stroke: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='ellipse".($i+1)."_stroke' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

}

print "</table>";

print p;

print "<table border>";

for (my $i=0; $i<$lines; $i++) {

	print "<TR><TD><B>Line ".($i+1)." x1: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_x1' VALUE='".(0+$i*5)."' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Line ".($i+1)." y1: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_y1' VALUE='".(450+$i*5)."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	print "<TR><TD><B>Line ".($i+1)." x2: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_x2' VALUE='".(450+$i*5)."' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Line ".($i+1)." y2: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_y2' VALUE='".(0+$i*5)."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	$col = int(rand @cols-1);
	print "<TR><TD><B>Line ".($i+1)." fill: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_fill' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD>\n";
	$col = int(rand @cols-1);
	print "<TD><B>Line ".($i+1)." stroke: </B></TD>\n";
	print "<TD><INPUT TYPE='text' NAME='line".($i+1)."_stroke' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

}

print "</table>";

print p;

print "<table border>";

for (my $i=0; $i<$texts; $i++) {

	print "<TR><TD><B>Text ".($i+1)." x: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_x' VALUE='75' SIZE=10 MAXLENGTH=10></TD>\n";
	print "<TD><B>Text ".($i+1)." y: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_y' VALUE='".(($i*50)+(500*(($i+1)/($texts+1))))."' SIZE=10 MAXLENGTH=10></TD></TR>\n";	
	print "<TR><TD><B>Text ".($i+1)." Font family: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_font' VALUE='Helvetica' SIZE=10 MAXLENGTH=20></TD>\n";
	print "<TD><B>Text ".($i+1)." Font size: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_size' VALUE='24' SIZE=10 MAXLENGTH=10></TD>\n";

	$col = int(rand @cols-1);
	print "<TR><TD><B>Text ".($i+1)." fill: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_fill' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD>\n";
	$col = int(rand @cols-1);
	print "<TD><B>Text ".($i+1)." stroke: </B></TD>\n";
	print "<TD colspan=1><INPUT TYPE='text' NAME='text".($i+1)."_stroke' VALUE='".($cols[$col])."' SIZE=10 MAXLENGTH=10></TD></TR>\n";

	print "<TR><TD><B>Text ".($i+1)." message: </B></TD>\n";
	print "<TD colspan=3><INPUT TYPE='text' NAME='text".($i+1)."_msg' VALUE='SVG-pl Customisable CGI Demo' SIZE=40 MAXLENGTH=100></TD>\n";

}

print "</table>";

} # end if else

print p;

print table(
	{-border=>0, -cellspacing=>5, -cellpadding=>5},
	Tr(td(submit("Done")), td(reset("Reset")))
);

print "\n</CENTER>";

print "</B></FONT>\n";
print end_form, hr;

print end_html;
