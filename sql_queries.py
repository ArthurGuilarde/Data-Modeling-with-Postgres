# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS public.songplays;"
user_table_drop = "DROP TABLE IF EXISTS public.users;"
song_table_drop = "DROP TABLE IF EXISTS public.songs;"
artist_table_drop = "DROP TABLE IF EXISTS public.artists;"
time_table_drop = 'DROP TABLE IF EXISTS public."time";'

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE public.songplays (
    songplay_id serial,
    start_time timestamp,
    user_id character varying(100),
    level character varying(100),
    song_id character varying(100),
    artist_id character varying(100),
    session_id character varying(100),
    location character varying(100),
    user_agent character varying(200)
);
ALTER TABLE ONLY public.songplays
    ADD CONSTRAINT songplays_pk PRIMARY KEY (songplay_id);
""")
# ADD CONSTRAINT songplays_fk_artist FOREIGN KEY (artist_id) REFERENCES public.artists(artist_id) ON UPDATE CASCADE,
# ADD CONSTRAINT songplays_fk_song FOREIGN KEY (song_id) REFERENCES public.songs(song_id) ON UPDATE CASCADE,
# ADD CONSTRAINT songplays_fk_time FOREIGN KEY (start_time) REFERENCES public."time"(start_time) ON UPDATE CASCADE,
# ADD CONSTRAINT songplays_fk_user FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE;
user_table_create = ("""
CREATE TABLE public.users (
    user_id character varying(100) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    gender character(1) NOT NULL,
    level character varying(100) NOT NULL
);
ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (user_id);
""")

song_table_create = ("""
CREATE TABLE public.songs (
    song_id character varying(100) NOT NULL,
    title character varying(100) NOT NULL,
    artist_id character varying(100) NOT NULL,
    year integer NOT NULL,
    duration float NOT NULL
);
ALTER TABLE ONLY public.songs
    ADD CONSTRAINT songs_pk PRIMARY KEY (song_id);
""")

artist_table_create = ("""
CREATE TABLE public.artists (
    artist_id character varying(100) NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(100) NOT NULL,
    latitude character varying(100),
    longitude character varying(100)
);
ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_pk PRIMARY KEY (artist_id);
""")

time_table_create = ("""
CREATE TABLE public."time" (
    start_time timestamp NOT NULL,
    hour integer NOT NULL,
    day integer NOT NULL,
    week integer NOT NULL,
    month integer NOT NULL,
    year integer NOT NULL,
    weekday integer NOT NULL
);   
ALTER TABLE ONLY public."time"
    ADD CONSTRAINT time_pk PRIMARY KEY (start_time);         
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO public.songplays
    (start_time, user_id, "level", song_id, artist_id, session_id, "location", user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
 INSERT INTO public.users
     (user_id, first_name, last_name, gender, "level")
     VALUES(%s, %s, %s, %s, %s)
     ON CONFLICT (user_id) 
     DO 
     UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO public.songs
    (song_id, title, artist_id, "year", duration)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO public.artists
    (artist_id, "name", "location", latitude, longitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;

""")


time_table_insert = ("""
INSERT INTO public."time"
    (start_time, "hour", "day", week, "month", "year", weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
select
	a.song_id,
	a.artist_id	
from
	songs a
join artists b on a.artist_id = b.artist_id 
where 
    a.title = %s
    and b."name" = %s
    and a.duration  = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, time_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]