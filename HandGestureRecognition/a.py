import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    input("Press Enter when ready...")

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                                cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
        # ret, frame = cap.read()
        # cv2.putText(frame, 'Ready? Press "q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
        #             cv2.LINE_AA)
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(25) == ord('q'):
        #     break
        # Save the frame when any key is pressed
        # if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
            print('Image {} saved for class {}'.format(counter, j))
            counter += 1


        # Break the loop if 'q' is pressed
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
