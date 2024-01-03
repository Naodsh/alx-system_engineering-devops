#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Extract the argument
text = ARGV[0]

# Define the regular expression
pattern = /School/

# Match the pattern in the given text
match = text.match(pattern)

# Output the result
puts match
