# MongoDB-IoT-Application
<p>A small application for a smart home IoT system using MongoDB as the database. I made this project to learn more about NoSQL databases. The implementation features a MongoDB database architecture with two shards and replica sets. The database is easily set up using the docker compose .yaml files.</p>
<p>The database setup is paired with a Flask API which provides complete CRUD functionality over the main collection in the database. The queries.mongodb in the App folder containes examples of a few advance aggregation you can perform on the database, once set-up and populated. In addition, while is running, the Flask server inserts some sensor reading into the database every 15 seconds, for simulation purposes.</p>
<br>
<sub>The build requires Python 3 or higher, Flask, Flask-APScheduler and Pymongo.<sub>

<p>
To set up the entire project:
<ol>
  <li>Run the .yaml files for Docker, in the order compose, servers then mongos.</li>
  <li>Set up the replica sets for the config servers, then for the nodes per each shard. Set up the sharding routers (monogs). All these instructions are in the .md in the Database Setup forlder. (P.S. I recommend to type the mongoshell commands yourself rather than echoing them through the Docker CLI.)</li>
  <li>Test the database installation using the VSCode MongoDB playground in the Database Setup folder</li>
  <li>Run the Init_collections.py script in the DataSetup folder to initialise all the collections and some sample data.</li>
  <li>Start the Flask server from app.py in the App folder.</li>
  <li>Enjoy :) build and customise to your liking*.</li>
</ol>
<sup>*The author of this project is not liable under any legal (or illegal) circumstances for any medical or mental injury you may suffer while attempting to replicate this project's functionality!</sup>
</p>

After you set up the MongoDB cluster, your Docker should look like this:
<br>
<img src="https://raw.githubusercontent.com/MihaiNastase/MongoDB-IoT-Application/main/dockerCompose.PNG" width="700" alt="Docker Compose">

<br>

The Docker cluster has the following architecture:
<br>
<img src="https://raw.githubusercontent.com/MihaiNastase/MongoDB-IoT-Application/main/IoT_Schema-Server%20Architecture_detail.png" width="700" alt="Server cluster">

<br>

And the DataSetup code (Along with the Flask server) is responsible for initialising the IoT database following the schema:

<br>
<img src="https://raw.githubusercontent.com/MihaiNastase/MongoDB-IoT-Application/main/IoT_Schema-Schema1.png" width="700" alt="Database schema">
