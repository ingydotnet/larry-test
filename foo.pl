#!/usr/bin/env perl

printf "Number of arguments: %s\n", scalar @ARGV;

for $arg (@ARGV) {
  print ">>> $arg\n"
}
