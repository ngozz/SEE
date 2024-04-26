import time

def calculate_salary_expense(salaries, staff_counts):
    total_expense = sum(salary * count for salary, count in zip(salaries, staff_counts))
    average_salary = total_expense / sum(staff_counts)
    average_salary_per_hour = average_salary / 160
    return total_expense, average_salary, average_salary_per_hour

def calculate_factors(ratings):
    # Đánh giá cho từng thành viên
    member_factors = [
        {'name': 'RUP application', 'weight': 1.5},
        {'name': 'Similar application experience', 'weight': 0.5},
        {'name': 'Object-oriented experience', 'weight': 1},
        {'name': 'Leadership ability', 'weight': 0.5},
        {'name': 'Dynamism', 'weight': 1}
    ]
    
    # Đánh giá chung cho Dự án
    project_factors = [
        {'name': 'Requirements stability', 'weight': 2},
        {'name': 'Part-time workers', 'weight': -1},
        {'name': 'Difficult programming language', 'weight': -1}
    ]
    
    # Tính toán hệ số tác động môi trường và nhóm làm việc (EFW)
    EFW = sum(member_factors[i]['weight'] * ratings[i] for i in range(5))
    EFW += sum(project_factors[i]['weight'] * ratings[i+5] for i in range(3))
    
    # Tính toán hệ số phức tạp về môi trường (EF)
    EF = 1.4 + (-0.03 * EFW)
    
    # Tính toán độ ổn định kinh nghiệm (ES)
    ES = 0
    for i in range(8):  # Loop through both member and project factors
        if i < 5:  # Member factor
            weight_rating = member_factors[i]['weight'] * ratings[i]
        else:  # Project factor
            weight_rating = project_factors[i-5]['weight'] * ratings[i]
        
        if weight_rating <= 0:
            ES += 0
        elif weight_rating <= 1:
            ES += 0.05
        elif weight_rating <= 2:
            ES += 0.1
        elif weight_rating <= 3:
            ES += 0.6
        else:
            ES += 1
    
    # Nội suy thời gian lao động (P)
    if ES < 1:
        P = 48
    elif ES < 3:
        P = 32
    else:
        P = 20

    return EFW, EF, ES, P

def slow_print(s, end='\n'):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print(end=end)

def slow_input(prompt):
    slow_print(prompt, end='')
    return input()
    
def main_menu():
    while True:
        slow_print("\n__________________________________________")
        slow_print("\nTrang chủ phần mềm. Chúc bạn một ngày tốt lành!\n")
        slow_print("0: Credits")
        slow_print("1: Tính toán hệ số")
        slow_print("2: Tính lương bình quân")
        slow_print("\nNhập 'exit' để thoát phần mềm khi ở trang chủ")
        slow_print("Nhập 'home' ở ngoài trang chủ để quay lại trang chủ")
        
        option = slow_input("Nhập lựa chọn: ")
        
        if option == '0':
            slow_print("\nCredits: Phần mềm được viết bởi Lê Duy Hiếu.")
        elif option == '1':
            calculate_factors_ui()
        elif option == '2':
            calculate_salary_expense_ui()
        elif option.lower() == 'exit':
            break
        else:
            slow_print("Lựa chọn không hợp lệ. Xin vui lòng thử lại.")

def calculate_factors_ui():
    # Nhập các giá trị xếp hạng từ người dùng
    ratings = []

    slow_print("\nNhập giá trị xếp hạng theo 8 tiêu chí sau với giá trị từ 0 đến 5, 5 là cao nhất, chấp nhận thập phân:\n")
    prompts = [
        "Có áp dụng qui trình phát triển phần mềm theo mẫu RUP và có hiểu biết về RUP hoặc quy trình phát triển phần mềm tương đương",
        "Có kinh nghiệm về ứng dụng tương tự",
        "Có kinh nghiệm về hướng đối tượng",
        "Có khả năng lãnh đạo Nhóm",
        "Tính chất năng động",
        "Độ ổn định của các yêu cầu",
        "Sử dụng các nhân viên làm bán thời gian",
        "Dùng ngôn ngữ lập trình loại khó"
    ]
    for i in range(8):
        if i == 0:
            slow_print("Đánh giá cho từng thành viên:\n")
        elif i == 5:
            slow_print("\nĐánh giá chung cho Dự án:\n")
        rating = slow_input(f"{prompts[i]}: ")
        if rating == 'home':
            return
        ratings.append(float(rating))
    
    # Tính toán và hiển thị kết quả
    EFW_result, EF, ES_result, P_result = calculate_factors(ratings)
    slow_print(f"Hệ số tác động môi trường và nhóm làm việc (EFW): {EFW_result}")
    slow_print(f"Hệ số phức tạp về môi trường (EF): {EF}")
    slow_print(f"Độ ổn định kinh nghiệm (ES): {ES_result}")
    slow_print(f"Nội suy thời gian lao động (P): {P_result}")

def calculate_salary_expense_ui():
    # Nhập số lượng nhóm từ người dùng
    num_groups = int(slow_input("\nNhập số lượng nhóm: "))

    # Nhập các giá trị lương và số lượng nhân viên từ người dùng
    salaries = []
    staff_counts = []

    slow_print("\nNhập mức lương/tháng và số lượng cán bộ:\n")
    for i in range(num_groups):
        salary = slow_input(f"Mức lương/tháng cho nhóm {i+1}: ")
        if salary == 'home':
            return
        salaries.append(float(salary))

        staff_count = slow_input(f"Số lượng cán bộ trong nhóm {i+1}: ")
        if staff_count == 'home':
            return
        staff_counts.append(int(staff_count))

    # Tính toán và hiển thị kết quả
    total_expense, average_salary, average_salary_per_hour = calculate_salary_expense(salaries, staff_counts)
    slow_print(f"Tổng chi lương/tháng: {total_expense}")
    slow_print(f"Mức lương bình quân/người/tháng: {average_salary}")
    slow_print(f"Mức lương bình quân/người/giờ: {average_salary_per_hour}")

if __name__ == "__main__":
    main_menu()