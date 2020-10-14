Machine cluster is a cluster of machine learning algorythms
it contains a 2-level rack
on the base level there are n machines that feed to final estimator
Eventually the metrics are calculated
The cluster has its own api that reports progress online.

The structure of the project is as follows:
Directory api contains independent application that responds on host ip through http protocol
It diplays html pages with short report as soon as started
http request GET hostIP:8008/[machine number]run starts machine if a numbered container is started
http request GET hostIP:8008/[machine number] shows the report of progress of the machine

Directory ml_machine contains the machine script
Starting file is machine_api. It starts a server that will respond to http command from main api [above].
Settings ajustable are in 2 files:
-ml_engine: declares sklearn classes and parameters to be used in the machine rack
-ml_setup: some additional parameters

Directory data is supposed to contain data files - separately train data set and target data set
This directory will be mapped to /var/data directory in every machine container.
Script collecting data is in ml_machine.main [first line] if needs adjusting

docker-compose file creates a single container
if more containers are to be set, ml_machine folder needs duplication and docker-compose file needs adjusting




