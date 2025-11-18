init_workflow_config_template = """
{
  "workflow_name": "workflow",
  "table_id": "0000",
  "state_column_key": "{state_column_key}",
  "participants_column_key": "{participants_column_key}",
  "nodes": [
    {
      "_id": "init",
      "type": "init",
      "name": "Start",
      "state": "",
      "participants": [],
      "next_node_id": "54420",
      "conditional_next_nodes": [],
      "other_node_ids": [],
      "node_form": {
        "readwrite_columns": [
          {
            "key": "0000"
          },
          {
            "key": "0Sd2"
          }
        ],
        "readonly_columns": []
      }
    },
    {
      "_id": "1",
      "type": "completed",
      "name": "Finished",
      "state": "",
      "is_send_finish_task_message": true,
      "finish_task_message": "",
      "node_form": {
        "readonly_columns": [
          {
            "key": "0000"
          },
          {
            "key": "0Sd2"
          }
        ],
        "readwrite_columns": []
      }
    },
    {
      "_id": "54420",
      "type": "normal",
      "name": "Node 1",
      "state": "",
      "participants": [
        "{test_username}"
      ],
      "participants_type": "static",
      "node_participants_column_key": "",
      "next_node_id": "1",
      "conditional_next_nodes": [],
      "other_node_ids": [],
      "node_form": {
        "readonly_columns": [],
        "readwrite_columns": [
          {
            "key": "0000"
          },
          {
            "key": "0Sd2"
          }
        ]
      }
    },
    {
      "_id": "canceled",
      "type": "canceled",
      "name": "Canceled"
    }
  ],
  "is_send_wechat_message": true,
  "account_id": 3
}
"""
