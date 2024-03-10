# 0-strace_is_your_friend.pp fixing typo

exec { 'fix-apache-error':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}