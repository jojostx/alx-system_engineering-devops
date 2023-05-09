# Fixes bug that causes apache error

exec { 'repair incorrect import':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => [ '/bin', '/sbin' ]
}
