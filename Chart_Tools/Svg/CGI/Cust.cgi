#!/usr/local/bin/perl
# cgi-bin/Cust.cgi

use CGI qw(:standard);

print header, start_html(
	-TITLE => "SVG CGI Test",
	-BGCOLOR => "white",
	-TEXT => "navy"
);

### Customise.cgi - Customisable Demo ###

BEGIN {
	$SVG_LIB = $ENV{"SVG_LIB"};
	unshift (@INC, $SVG_LIB);
}

use Svg::File;
use Svg::Graphics;

my $filetime;
my @time = localtime(time);

foreach (@time) {$filetime = $_.$filetime}

my $filenumber = int(rand 9999) + 1;
my $filename = "../public_html/svg/$filetime$filenumber.svg";

my $svg = Svg::File->new($filename);
$svg->open("public", "encoding", "iso-8859-1", "silent");

my $rects = param("hidden_rects");
my $circles = param("hidden_circles");
my $ellipses = param("hidden_ellipses");
my $lines = param("hidden_lines");
my $texts = param("hidden_texts");

my $viewbox_x1 = param("viewbox_x1");
my $viewbox_y1 = param("viewbox_y1");
my $viewbox_x2 = param("viewbox_x2");
my $viewbox_y2 = param("viewbox_y2");

my $svg_width = param("svg_width");
my $svg_height = param("svg_height");
my $svg_x = param("svg_x");
my $svg_y = param("svg_y");

my $bg_x = param("bg_x");
my $bg_y = param("bg_y");
my $bg_width = param("bg_width");
my $bg_height = param("bg_height");
my $bg_fill = param("bg_fill");
my $bg_stroke = param("bg_stroke");

my @rect_x;
my @rect_y;
my @rect_width;
my @rect_height;
my @rect_fill;
my @rect_stroke;

for (my $i=0; $i<$rects; $i++) {
	my $x = param("rect".($i+1)."_x");
	my $y = param("rect".($i+1)."_y");
	my $width = param("rect".($i+1)."_width");
	my $height = param("rect".($i+1)."_height");
	my $fill = param("rect".($i+1)."_fill");
	my $stroke = param("rect".($i+1)."_stroke");
	push(@rect_x,$x);
	push(@rect_y,$y);
	push(@rect_width,$width);
	push(@rect_height,$height);
	push(@rect_fill,$fill);
	push(@rect_stroke,$stroke);
}

my @circle_cx;
my @circle_cy;
my @circle_r;
my @circle_fill;
my @circle_stroke;

for (my $i=0; $i<$circles; $i++) {
	my $cx = param("circle".($i+1)."_cx");
	my $cy = param("circle".($i+1)."_cy");
	my $r = param("circle".($i+1)."_r");
	my $fill = param("circle".($i+1)."_fill");
	my $stroke = param("circle".($i+1)."_stroke");
	push(@circle_cx,$cx);
	push(@circle_cy,$cy);
	push(@circle_r,$r);
	push(@circle_fill,$fill);
	push(@circle_stroke,$stroke);
}

my @ellipse_cx;
my @ellipse_cy;
my @ellipse_rx;
my @ellipse_ry;
my @ellipse_fill;
my @ellipse_stroke;

for (my $i=0; $i<$ellipses; $i++) {
	my $cx = param("ellipse".($i+1)."_cx");
	my $cy = param("ellipse".($i+1)."_cy");
	my $rx = param("ellipse".($i+1)."_rx");
	my $ry = param("ellipse".($i+1)."_ry");
	my $fill = param("ellipse".($i+1)."_fill");
	my $stroke = param("ellipse".($i+1)."_stroke");
	push(@ellipse_cx,$cx);
	push(@ellipse_cy,$cy);
	push(@ellipse_rx,$rx);
	push(@ellipse_ry,$ry);
	push(@ellipse_fill,$fill);
	push(@ellipse_stroke,$stroke);
}

my @line_x1;
my @line_y1;
my @line_x2;
my @line_y2;
my @line_fill;
my @line_stroke;

for (my $i=0; $i<$lines; $i++) {
	my $x1 = param("line".($i+1)."_x1");
	my $y1 = param("line".($i+1)."_y1");
	my $x2 = param("line".($i+1)."_x2");
	my $y2 = param("line".($i+1)."_y2");
	my $fill = param("line".($i+1)."_fill");
	my $stroke = param("line".($i+1)."_stroke");
	push(@line_x1,$x1);
	push(@line_y1,$y1);
	push(@line_x2,$x2);
	push(@line_y2,$y2);
	push(@line_fill,$fill);
	push(@line_stroke,$stroke);
}

my @text_x;
my @text_y;
my @text_font;
my @text_size;
my @text_fill;
my @text_stroke;
my @text_msg;

for (my $i=0; $i<$texts; $i++) {
	my $x = param("text".($i+1)."_x");
	my $y = param("text".($i+1)."_y");
	my $font = param("text".($i+1)."_font");
	my $size = param("text".($i+1)."_size");
	my $fill = param("text".($i+1)."_fill");
	my $stroke = param("text".($i+1)."_stroke");
	my $msg = param("text".($i+1)."_msg");
	push(@text_x,$x);
	push(@text_y,$y);
	push(@text_font,$font);
	push(@text_size,$size);
	push(@text_fill,$fill);
	push(@text_stroke,$stroke);
	push(@text_msg,$msg);
}

my $g = $svg->beginGraphics();

$g->b("svg", "viewBox", "$viewbox_x1 $viewbox_y1 $viewbox_x2 $viewbox_y2", "width", "450", "height", "450", "xval", $svg_x, "yval", $svg_y);

	$g->d("rect", "id", "BG", "xval", $bg_x, "yval", $bg_y, "width", $bg_width, "height", $bg_height, "style", "fill:$bg_fill;stroke:$bg_stroke");

	for ($i=0; $i<$rects; $i++) {
		$g->d("rect", "xval", $rect_x[$i], "yval", $rect_y[$i], "width", $rect_width[$i], "height", $rect_height[$i], "style", "fill:$rect_fill[$i];stroke:$rect_stroke[$i]");
	}

	for ($j=0; $j<$circles; $j++) {
		$g->d("circle", "cx", $circle_cx[$j], "cy", $circle_cy[$j], "r", $circle_r[$j], "style", "fill:$circle_fill[$j];stroke:$circle_stroke[$j]");
	}

	for ($k=0; $k<$ellipses; $k++) {
		$g->d("ellipse", "cx", $ellipse_cx[$k], "cy", $ellipse_cy[$k], "rx", $ellipse_rx[$k], "ry", $ellipse_ry[$k], "style", "fill:$ellipse_fill[$k];stroke:$ellipse_stroke[$k]");
	}

	for ($m=0; $m<$lines; $m++) {
		$g->d("line", "x1", $line_x1[$m], "y1", $line_y1[$m], "x2", $line_x2[$m], "y2", $line_y2[$m], "style", "fill:$line_fill[$m];stroke:$line_stroke[$m]");
	}

	for ($l=0; $l<$texts; $l++) {
		$g->b("text", "xval", $text_x[$l], "yval", $text_y[$l], "style", "font-family:$text_font[$l];font-size:$text_size[$l]");
			$g->printTxt($text_msg[$l]);
		$g->e();
	}

$g->e();

# clean up
$svg->close($g);

$filename = "http://cs.nott.ac.uk/~jxm/svg/$filetime$filenumber.svg";

print "<CENTER><EMBED SRC=\"$filename\" WIDTH=\"80%\" HEIGHT=\"80%\">";

print "<P><A HREF='javascript:window.history.go(-2)'>Start Over Again</A></CENTER>";

print end_html;

opendir (DIR, "../public_html/svg/");
my @files = readdir(DIR);
closedir(DIR);

my @systime = localtime(time);
my $regexp = "$systime[8]$systime[7]$systime[6]$systime[5]$systime[4]$systime[3]$systime[2]";

foreach (@files) {
	chomp;
	if (!($_ =~ /^$regexp|^\.{1,2}/)) {system "rm ../public_html/svg/$_"}
}
