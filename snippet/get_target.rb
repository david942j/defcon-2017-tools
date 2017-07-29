def get_target(default_port)
  host = ARGV[0] || '127.0.0.1'
  port = (ARGV[1] || default_port).to_i
  [host, port]
end
