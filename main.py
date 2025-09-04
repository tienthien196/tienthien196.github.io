import usb.core
import usb.util

# Tìm tất cả các thiết bị USB được kết nối
devs = usb.core.find(find_all=True)

# Lặp qua từng thiết bị và in thông tin
if not devs:
    print("Không tìm thấy thiết bị USB nào.")
else:
    print("Danh sách các thiết bị USB đã kết nối:")
    for dev in devs:
        try:
            # Lấy thông tin về nhà sản xuất và sản phẩm
            manufacturer = usb.util.get_string(dev, dev.iManufacturer)
            product = usb.util.get_string(dev, dev.iProduct)
            serial = usb.util.get_string(dev, dev.iSerialNumber)
            
            print(f"  ID: {hex(dev.idVendor)}:{hex(dev.idProduct)}")
            print(f"  Nhà sản xuất: {manufacturer}")
            print(f"  Sản phẩm: {product}")
            if serial:
                print(f"  Số serial: {serial}")
            print("---")
        except Exception as e:
            # Một số thiết bị có thể không cho phép truy cập thông tin này
            print(f"  ID: {hex(dev.idVendor)}:{hex(dev.idProduct)}")
            print("  Không thể lấy thông tin chi tiết. (Lỗi: {})".format(e))
            print("---")