{
  "config": {
    "log": "debug"
  },
  "source" : {
    "file": { "path": "/home/amaury/coleta/n1/egos/friends_data_full.json" }
  },
  "extractor" : {
    "json": []
  },
  "transformers" : [
    { "merge": { "joinFieldName": "id", "lookup": "V_ego.ego_id" } },
    { "vertex": { "class": "V_ego"} },
    { "vertex": { "class": "V_alter"} },
    { "edge": {
      "class": "ego_friends",
      "joinFieldName": "friends",
      "lookup": "V_alter.alter_id",
      "unresolvedLinkAction": "CREATE"
    	}
    }
  ],
  "loader" : {
    "orientdb": {
      "dbURL": "plocal:/opt/orientdb/databases/twitter_teste",
      "dbUser": "admin",
      "dbPassword": "admin",
      "dbAutoDropIfExists": false,
      "dbAutoCreate": false,
      "standardElementConstraints": false,
      "tx": false,
      "wal": false,
      "batchCommit": 1000000,
      "dbType": "graph",
      "classes": [{"name": "V_ego", "extends":"V"}, {"name": "V_alter", "extends":"V"}, {"name": 'ego_friends', "extends":"E"}],
      "indexes": [{"class":"V_ego", "fields":["V_ego.ego_id:string"], "type":"UNIQUE_HASH_INDEX" }],
      "indexes": [{"class":"V_alter", "fields":["V_alter.alter_id:string"], "type":"UNIQUE_HASH_INDEX" }]
    }
  }
}