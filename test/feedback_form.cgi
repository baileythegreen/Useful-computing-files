#!/usr/bin/perlml

use CGI;

# Create a CGI.pm object
my $cgi = new CGI;

# Get the form data
my $email_address = "baileythegreen\@gmail.com"; #$cgi->param('email_address');
my $feedback = "This is an email."; #$cgi->param('feedback');

# Filter the form data
$email_address  = filter_email_header($email_address);
#$feedback = filter_form_data($feedback);

# Email the form data
open ( MAIL, "| /usr/sbin/sendmail -t -odq");
print MAIL << "EOF";
From: $email_address
To: baileythegreen\@gmail.com
Subject: Feedback Form Submission
$feedback
.
EOF
close ( MAIL );

# Print the HTTP header
print $cgi->header(-type => 'text/html');

# Print the HTML thank you page
print <<HTML_PAGE;
<html>
<head>
<title>Thank You</title>
</head>
<body>
<h1>Thank You</h1>
<p>Thank you for your feedback.</p>
</body>
</html>
HTML_PAGE

# Functions to filter the form data

sub filter_email_header
{
my $form_field = shift;  
#$form_field = filter_form_data($form_field);  
$form_field  =~ s/[nr|!\/<>^$%*&]+/ /g;  

return $form_field ;
}

#sub filter_form_data
#{  my $form_field = shift;
#$form_field  =~ s/From://gi;  
#$form_field  =~ s/To://gi;  
#$form_field  =~ s/BCC://gi;  
#$form_field  =~ s/CC://gi;  
#$form_field  =~ s/Subject://gi;  
#$form_field  =~ s/Content-Type://gi;

#return $form_field ;
#}
