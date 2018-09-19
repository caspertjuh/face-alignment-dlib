import cv2, dlib, argparse, os
from utils import extract_left_eye_center, extract_right_eye_center, get_rotation_matrix, crop_image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Align faces in image')
    parser.add_argument('input', type=str, help='')
    parser.add_argument('output', type=str, help='')
    parser.add_argument('--scale', metavar='S', type=int, default=1, help='an integer for the accumulator')
    args = parser.parse_args()

    input_image_folder = args.input
    output_image_folder = args.output
    scale = args.scale

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    directory = os.fsencode(input_image_folder)

    list = os.listdir(directory)
    maxFiles = len(list)
    counter = 0

    for file in os.listdir(directory):
        counter = counter + 1
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".bmp"):
            print('transforming ' + str(counter) + '/' + str(maxFiles) + ': '+ filename)
            img = cv2.imread(input_image_folder + '/' + filename, cv2.IMREAD_GRAYSCALE)
            height, width = img.shape[:2]
            s_height, s_width = height // scale, width // scale
            img = cv2.resize(img, (s_width, s_height))
            dets = detector(img, 1)
            for i, det in enumerate(dets):
                shape = predictor(img, det)
                left_eye = extract_left_eye_center(shape)
                right_eye = extract_right_eye_center(shape)

                M = get_rotation_matrix(left_eye, right_eye)
                rotated = cv2.warpAffine(img, M, (s_width, s_height), flags=cv2.INTER_CUBIC)

                cropped = crop_image(rotated, det)

                if filename.endswith('.jpg'):
                    output_image = filename.replace('.jpg', '_%i.jpg' % i)
                elif filename.endswith('.png'):
                    output_image = filename.replace('.png', '_%i.jpg' % i)
                elif filename.endswith('.jpeg'):
                    output_image = filename.replace('.jpeg', '_%i.jpg' % i)
                elif filename.endswith('.bmp'):
                    output_image = filename.replace('.bmp', '_%i.bmp' % i)
                else:
                    output_image = output_image_folder + ('_%i.jpg' % i)
                cv2.imwrite(output_image_folder + '/' + output_image, cropped)

            continue
        else:
            continue



