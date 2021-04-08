#!/usr/local/bin/perl
# cgi-bin/Text.cgi

print "Content-type: image/svg+xml\n\n";

### Text.cgi - Text Sample ###

# BEGIN lines
BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use CGI qw(:standard);

use Svg::File;				# USE lines
use Svg::Graphics;

my $svg = Svg::File->new("cgi");		# OPEN FILE lines
$svg->open("public","encoding","iso-8859-1","silent");	

my $g = $svg->beginGraphics();		# BEGIN GRAPHICS line

my $vbX = 800;
my $vbY = 600;

$g->b("svg","viewBox","0,0,$vbX,$vbY","width",$vbX/2,"height",$vbY/2);
  
  # set text environments
  $g->setFontSize("24");
  $g->setFontColor("blue");
  $g->setFontFamily("Helvetica-Bold");

  # draw single text string with two statements
  # with breaks at gap between words
  $g->b("text","xval",$vbX/10,"yval",$vbY/4,"doStyle");
	$g->printTxt("This is the ");
	$g->printTxt("first line");
  $g->e();

  # set text environments
  $g->setFontSize("16");
  $g->setFontColor("red");
  $g->setFontFamily("Courier");

  # draw single text string with three statements
  # with breaks at gaps between words
  $g->b("text","xval",$vbX/10,"yval",$vbY/4+20,"doStyle");
	$g->printTxt("And here ");
	$g->printTxt("comes ");
	$g->printTxt("the second");
  $g->e();

  # set text environments
  $g->setFontSize("12");
  $g->setFontColor("gray");
  $g->setFontFamily("Times-Bold");

  # draw single text string with four statements
  # with breaks between any characters
  $g->b("text","xval",$vbX/10,"yval",$vbY/4+40,"doStyle");
	$g->printTxt("Yo");
	$g->printTxt("u've guess");
	$g->printTxt("ed it..");
	$g->printTxt(". here's the third!");
  $g->e();

$g->e();

$svg->close($g);			# END line
