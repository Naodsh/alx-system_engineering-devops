#!/usr/bin/env ruby

# Define a method to extract information from log entries
def extract_info(log_entry)
  sender = log_entry.match(/\[from:([^ \]]+)/)[1]
  receiver = log_entry.match(/\[to:([^ \]]+)/)[1]
  flags = log_entry.match(/\[flags:([^ \]]+)/)[1]

  "#{sender},#{receiver},#{flags}"
end

# Read the log file and process each line
File.foreach("logfile.txt") do |line|
  if line.include?("Receive SMS") || line.include?("Sent SMS")
    puts extract_info(line)
  end
end
