# Data-minning
code in KTlab
# dantri.py
+ crawl dữ liệu thông tin các bài báo trên trang [dantri](https://dantri.com.vn)
+ thông tin các bài báo bao gồm title, ngày đăng, tác giả,tag,( có thể lấy được nội dung nhưng ko lấy vì dung lượng file lớn)
# phimmoi.py
+ crawl dữ liệu các bộ phim trên trang [phimmoizz](http://www.phimmoizz.net/) vào file json
+ thông tin các bộ phim gồm : thể loại , số tập, tóm tắt phim, link xem phim, keyword, thông tin chi tiết của phim
# amazone.py
+ crawl dữ liệu các thông tin sản phẩm trên trang [amazone](https://www.amazon.com/) vào file json
+ thông tin của sản phẩm gồm: tên sản phẩm, giá , phí ship, rate, customer_reply, description
# result
+ các kết quả được lưu trong file result
+ phimmoi : lấy được dữ liệu của 200 bộ phim
+ dantri : lấy dữ liệu của 8331 bài viết
+ amazone :lấy dữ liệu của 200 sản phẩm
# chạy code
+ chạy file run_crawler.py để bắt đầu crawl
