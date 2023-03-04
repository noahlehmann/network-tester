CREATE SEQUENCE t_speed_test_result_seq;

CREATE TABLE t_speed_test_result (
    id bigint primary key default nextval('t_speed_test_result_seq'),
    exec_timestamp timestamp not null,
    successful boolean not null,
    ping_ms numeric,
    download_mb numeric,
    upload_mb numeric,
    ip text,
    isp text,
    country text,
    lat double precision,
    lon double precision
);

CREATE SEQUENCE t_log_seq;

CREATE TABLE t_log (
    id bigint primary key default nextval('t_log_seq'),
    log_timestamp timestamp not null,
    level text,
    msg text,
    fk_test bigint not null references t_speed_test_result(id)
);