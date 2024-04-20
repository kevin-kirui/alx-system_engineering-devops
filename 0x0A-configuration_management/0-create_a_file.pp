# create a file
file { '/tmp/school':

    mode    => '0744';

    owner   => 'www-date',

    group   => 'www-data',

    content => 'I love puppet'

}
