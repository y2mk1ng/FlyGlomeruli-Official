import cv2, os, numpy

path_ans = input('The file path of your ANSWERS: ')
path_result_1 = input('The file path of your PREDTCTION RESULTS (please enter the string before any numbers): ')
path_result_here = input('The directory where you want to save your ANALYSIS RESULTS FROM HERE: ')

## accuracy part
import cv2, numpy
def intersect_xor():
    for _num in range(1, 3):
        for img_num in range(0, 30):
            img1 = numpy.array(cv2.imread(path_ans + str(img_num) + '.png', 0))
            img2 = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_combined.png', 0))
            diff = img2 - img1
            diff_inv = img1 - img2
            intersection = cv2.bitwise_and(img1, img2, mask = None)
            img_diff = cv2.imwrite(path_result_1 + str(_num) + '/' + str(img_num) + '_diff.png', diff)
            img_diff_inv = cv2.imwrite(path_result_1 + str(_num) + '/' + str(img_num) + '_diff_inv.png', diff_inv)
            img_intersect = cv2.imwrite(path_result_1 + str(_num) + '/' + str(img_num) + '_intersect.png', intersection)
def colorize():
    for _num in range(1, 3):
        for img_num in range(0, 30):
            img_diff_r = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_diff.png'))
            img_diff_inv_r = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_diff_inv.png'))
            img_intersect = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_intersect.png'))
            red, green, blue = img_diff_r.T
            red_inv, green_inv, blue_inv = img_diff_inv_r.T
            red_intr, green_intr, blue_intr = img_intersect.T
            white_areas = (red == 255) & (green == 255) & (blue == 255)
            white_areas_inv = (red_inv == 255) & (green_inv == 255) & (blue_inv == 255)
            white_areas_intr = (red_intr == 255) & (green_intr == 255) & (blue_intr == 255)
            img_diff_r[...][white_areas.T] = (0, 0, 255) ###BGR mode
            img_diff_inv_r[...][white_areas_inv.T] = (255, 0, 0)
            img_intersect[...][white_areas_intr.T] = (0, 255, 0)
            cv2.imwrite(path_result_here + str(_num) + '_' + str(img_num) + '_diff_red.png', img_diff_r)
            cv2.imwrite(path_result_here + str(_num) + '_' + str(img_num) + '_diff_inv_blue.png', img_diff_inv_r)
            cv2.imwrite(path_result_here + str(_num) + '_' + str(img_num) + '_TP_green.png', img_intersect)
def add_up():
    for _num in range(1, 3):
        for img_num in range(0, 30):
            img_red = numpy.array(cv2.imread(path_result_here + str(_num) + '_' + str(img_num) + '_diff_red.png', 1))
            img_blue = numpy.array(cv2.imread(path_result_here + str(_num) + '_' + str(img_num) + '_diff_inv_blue.png', 1))
            img_green = numpy.array(cv2.imread(path_result_here + str(_num) + '_' + str(img_num) + '_TP_green.png', 1))
            img_addup_br = cv2.bitwise_or(img_red, img_blue, mask = None)
            img_addup = cv2.bitwise_or(img_green, img_addup_br, mask = None)
            cv2.imwrite(path_result_here + str(_num) + '_' + str(img_num) + '_addup.png', img_addup)
def accuracy():
    intersect_xor()
    colorize()
    add_up()

## statistics part
def FP(_num, img_num):
    global fp_rate
    img_diff_r = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_diff.png', 0))
    fp = numpy.count_nonzero(img_diff_r == 255)
    fp_rate = fp / (512 * 512)
    print('FP_rate of '  + str(_num) + '-' + str(img_num) + ' =', fp_rate)
    with open(path_result_here + '/Z_' + str(_num) + '_' + str(img_num) + '_diff_FP.txt', 'w') as f:
        f.write(str(fp_rate))
        f.close()
def FN(_num, img_num):
    global fn_rate
    img_diff_inv_r = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_diff_inv.png', 0))
    fn = numpy.count_nonzero(img_diff_inv_r == 255)
    fn_rate = fn / (512 * 512)
    print('FN_rate of '  + str(_num) + '-' + str(img_num) + ' =', fn_rate)
    with open(path_result_here + '/Z_' + str(_num) + '_' + str(img_num) + '_diff_inv_FN.txt', 'w') as f:
        f.write(str(fn_rate))
        f.close()
def TP(_num, img_num):
    global tp_rate
    img_intersect_r = numpy.array(cv2.imread(path_result_1 + str(_num) + '/' + str(img_num) + '_intersect.png', 0))
    tp = numpy.count_nonzero(img_intersect_r == 255)
    tp_rate = tp / (512 * 512)
    print('TP_rate of '  + str(_num) + '-' + str(img_num) + ' =', tp_rate)
    with open(path_result_here + '/Z_' + str(_num) + '_' + str(img_num) + '_intersect_TP.txt', 'w') as f:
        f.write(str(tp_rate))
        f.close()
def TN(_num, img_num):
    global tn_rate
    unioned = numpy.array(cv2.imread(path_result_here + str(_num) + '_' + str(img_num) + '_addup.png', 0))
    arr_count = numpy.count_nonzero(unioned != 0)
    tn = (512*512) - arr_count
    tn_rate = tn / (512*512)
    print('TN_rate of ' + str(_num) + '-' + str(img_num) + ' =', tn_rate)
    with open(path_result_here + '/' + str(_num) + '_' + str(img_num) + '_TN.txt', 'w') as f:
        f.write(str(tn_rate))
        f.close()
def statistics(_num, img_num):
    FPR = fp_rate / (fp_rate + tn_rate)
    print('FPR of ' + str(_num) + '-' + str(img_num) + '= ', FPR)
    TPR = tp_rate / (tp_rate + fn_rate)
    print('TPR of ' + str(_num) + '-' + str(img_num) + '= ',TPR)
    ACC = (tp_rate + tn_rate) / (tp_rate + fn_rate + fp_rate + tn_rate)
    print('ACC of ' + str(_num) + '-' + str(img_num) + '= ', ACC)

def statistic_four_all():
    for _num in range(1, 3):
        for img_num in range(1, 30):
            FP(_num, img_num)
            FN(_num, img_num)
            TP(_num, img_num)
            TN(_num, img_num)
            statistics(_num, img_num)
## packed here
def main():
    accuracy()
    statistic_four_all()

if __name__ == '__main__':
    main()
