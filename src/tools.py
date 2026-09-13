"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Modifiy cho case QC agentic
    {
        "name": "query_qc_label",
        "description": (
            "Tra cứu kết quả kiểm định chất lượng của một ca gán nhãn"
            "2D/3D bằng mã label."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "label_id": {
                    "type": "string",
                    "description": "Mã ca gán nhãn, ex.'LB-3D-102'"
                }
            },
            "required": ["label_id"]
        }
    },
    
    # Second tool for writing ticket
    {
          "name": "create_rework_ticket",
          "description": (
              "Tạo phiếu Rework cho một ca gán nhãn đã không đạt "
              "kiểm định chất lượng."
          ),
          "parameters": {
              "type": "object",
              "properties": {
                  "label_id": {
                      "type": "string",
                      "description": "Mã ca gán nhãn cần sửa lại"
                  },
                  "reason": {
                      "type": "string",
                      "description": "Mô tả lỗi khiến ca gán nhãn cần Rework"
                  },
                  "priority": {
                      "type": "string",
                      "description": "Mức độ ưu tiên của phiếu Rework",
                      "enum": ["LOW", "MEDIUM", "HIGH"]
                  }
              },
              "required": ["label_id", "reason", "priority"]
          }
      }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

QC_DATABASE = {
      "LB-3D-102": {
          "data_type": "3D",
          "qc_status": "FAILED",
          "defect_type": "Incorrect 3D bounding box",
          "severity": "HIGH",
          "rework_required": True
      },
      "LB-2D-201": {
          "data_type": "2D",
          "qc_status": "PASSED",
          "defect_type": None,
          "severity": None,
          "rework_required": False
      }
  }



def execute_query_qc_label(label_id: str) -> str: 
    """Check if the label exist in the DB or not"""
    label_id = label_id.strip().upper()
    record = QC_DATABASE.get(label_id)

    if not record:
        return json.dump({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy được ca gán nhãn {label_id}"
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCESS",
        "label_id": label_id,
        "data": record
    }, ensure_ascii=False)

def execute_create_rework_ticket(
      label_id: str,
      reason: str,
      priority: str
  ) -> str:
      label_id = label_id.strip().upper()
      record = QC_DATABASE.get(label_id)

      if not record:
          return json.dumps({
              "status": "NOT_FOUND",
              "message": f"Không tìm thấy ca gán nhãn '{label_id}'."
          }, ensure_ascii=False)

      if not record["rework_required"]:
          return json.dumps({
              "status": "REJECTED",
              "message": (
                  f"Ca gán nhãn '{label_id}' đã đạt QC; "
                  "không cần tạo phiếu Rework."
              )
          }, ensure_ascii=False)

      return json.dumps({
          "status": "SUCCESS",
          "ticket_id": f"RW-{label_id}",
          "label_id": label_id,
          "reason": reason,
          "priority": priority,
          "message": f"Đã tạo phiếu Rework cho '{label_id}'."
      }, ensure_ascii=False)



# Router gọi tool thực tế
TOOL_ROUTER = {
    "query_qc_label": execute_query_qc_label,
    "create_rework_tickey": execute_create_rework_ticket
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
