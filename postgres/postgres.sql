CREATE TABLE error_log (
  timestamp timestamp with time zone default current_timestamp,
  error text,
  message text,
  filename text,
  line_number integer
);