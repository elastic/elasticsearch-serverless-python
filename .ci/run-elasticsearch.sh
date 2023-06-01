#!/usr/bin/env bash
#
environment=($(cat <<-END
  --env ELASTIC_PASSWORD=changeme
  --env node.name=elasticsearch-serverless
  --env cluster.name=elasticsearch-serverless
  --env cluster.initial_master_nodes=elasticsearch-serverless
  --env discovery.seed_hosts=instance
  --env cluster.routing.allocation.disk.threshold_enabled=false
  --env bootstrap.memory_lock=true
  --env node.attr.testattr=test
  --env path.repo=/tmp
  --env repositories.url.allowed_urls=http://snapshot.test*
  --env action.destructive_requires_name=false
  --env ingest.geoip.downloader.enabled=false
  --env cluster.deprecation_indexing.enabled=false
  --env xpack.security.enabled=false
  --env xpack.security.http.ssl.enabled=false
END
))

export DETACH=${DETACH-false}

docker run \
       --name elasticsearch-serverless \
       --network elastic \
       --env "ES_JAVA_OPTS=-Des.serverless=true -Xms1g -Xmx1g -da:org.elasticsearch.xpack.ccr.index.engine.FollowingEngineAssertions" \
       "${environment[@]}" \
       --volume serverless-data:/usr/share/elasticsearch/data \
       --publish 9200:9200 \
       --ulimit nofile=65536:65536 \
       --ulimit memlock=-1:-1 \
       --detach=$DETACH \
       --rm \
       docker.elastic.co/elasticsearch/elasticsearch:$STACK_VERSION;
