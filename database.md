
User table will contain 
    -a unique user_id, 
    - email and password (hashed and salted) for auth purposes
    - payment details  (needs to properly encrypted or uses a trusted 3rd like payfast)

User Table:
    user_id int (primary key)
    username varchar(100)
    email varchar(100)
    password varchar(100)
    card_number int

Worker table will contain
- worker id for indexing
- Avaible times
- Their location (for job tracking)

Worker Table:

    worker_id (primary key)
    availability
    location
    contact

Job Table will contain:
- id for indexing
- user_id in reference to user table
- worker_id in refernce to worker table
- amount
- required date

Job:

    job_id (primary key)
    user_id (foreign key referencing User table)
    job_title
    job_description
    amount
    required_date


Rating table will contain
- id 
- worker id to note which worker was on the job
- job id to note which task was performed
- rating out of 5 starts
- comment (optional)


Rating Table:

    rating_id (primary key)
    worker_id (foreign key )
    job_id (foreign key)
    rating int
    comment varchar(100)