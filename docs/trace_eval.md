# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Quang Minh  
> **Mã Sinh Viên / Mã Học viên:** 2A2020602440  
> **Chủ đề Lựa chọn:** Trợ lý Kiểm định Chất lượng (QC Assistant)

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Agent này sẽ phải xác định mã lỗi dựa ào các loại dữ liệu từ 2D đến 3D, sau đó sẽ phải tra cứu thông tin, đánh giá và quyết định xem có cần kiểm tra lại hay không |
| **2. Tool Interaction** | 5 / 5 | Hệ thống này sẽ cần tối thiểu hai công cụ: công cụ tra cứu ca lỗi và công cụ tạo phiếu để kiểm tra lại. Các công cụ được gọi thông qua MCP server và có thể kết nối với cơ sở dữ liệu |
| **3. Dynamic Decision** | 5 / 5 | Nếu không tìm thầy ca lỗi thì sẽ phải kiểm tra lại mã của gãn dán, rồi kiểm tra xem đã đủ điều kiện hay chưa để có thể viết phiếu để yêu cầu rework lại quá trình. Nếu phiếu đã tồn tại, agent cũng phải kiểm tra xem để tránh lặp |
| **4. Long Horizon Goal** | 2 / 5 | Hệ thống cần duy trì mục tiêu xử lý xuyên suốt nhiều bước, tuy nhiêu tổng các bước vẫn còn đang ngắn |
| **TỔNG ĐIỂM AGENTIC FIT** | ** 16 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu kết quả kiểm định chất lượng của ca gán nhãn LB-3D-102.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "query_qc_label",
    "arguments": {
      "label_id": "LB-3D-102"
    },
    "observation": {
      "status": "SUCESS",
      "label_id": "LB-3D-102",
      "data": {
        "data_type": "3D",
        "qc_status": "FAILED",
        "defect_type": "Incorrect 3D bounding box",
        "severity": "HIGH",
        "rework_required": true
      }
    },
    "latency_ms": 5476.08
  },
  {
    "step": 2,
    "query": "Hãy tra cứu kết quả kiểm định chất lượng của ca gán nhãn LB-3D-102.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Phản hồi từ công cụ: {\"status\": \"SUCESS\", \"label_id\": \"LB-3D-102\", \"data\": {\"data_type\": \"3D\", \"qc_status\": \"FAILED\", \"defect_type\": \"Incorrect 3D bounding box\", \"severity\": \"HIGH\", \"rework_required\": true}}",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 2 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 2 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
