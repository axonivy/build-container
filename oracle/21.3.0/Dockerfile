FROM docker-registry.ivyteam.io/oracle/database:21.3.0-se2
ADD --chown=oracle:dba data /opt/oracle/oradata
ENV ORACLE_SID=ORASID
ENV ORACLE_PDB=ORAPDB
ENV ORACLE_CHARACTERSET=AL32UTF8
ENV ORACLE_PWD=nimda
