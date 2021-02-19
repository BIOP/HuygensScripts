import os 

# to make use of ttictoc, you need to add the path, edit> pref > directories
#import ttictoc
#ttictoc.tic()

maindir = "E://Test_GPU-HPro//AB//Viv//"

# to avoid pop up warning
huOpt.verb(mode = "silent")

# here we load an empty image with the right microscopic parameters 
# to transfer them to each time-point.
# (seems as an easier solution than settings all the parameters)
micparam_path = os.path.join(maindir,"psf_2chs_TB.ics")
if os.path.exists(micparam_path ):
    microParam = image(path=micparam_path)
    #microParam.show()

#where images are  
image_dir = os.path.join(maindir,"Raw_from_Machine")

#where output images will be saved
output_path = os.path.join(image_dir,"deconv")
if not os.path.exists(output_path):
    os.mkdir(output_path)
 
# create an empty image, 
# so the deconvolution is done using a theoretical psf based on Microscopic Parameters
psf = image()

for idx in range(1,2):
    # open the using time index (for now it opens both channels)
    # TODO fing why and how to control! 
    
    current_img_name = "t000"+str(idx)+"_Channel 1.tif"
    current_img_path = os.path.join(image_dir, current_img_name)
    
    if os.path.exists(current_img_path ):
        current_img = image(path= str(current_img_path))
        #current_img.show()
        
        # the microParam file contains info, pixel size , wavelength ..., 
        # so we apply Microscoppic Parameters to the current_img
            
        #do the deconvolution
        #result_img = current_img.cmle(psf , it = 50, snr = 2, q=0.01, bgMode="manual", bg=[0], brMode="auto")
        result_img = current_img.cmle(psf , it = 2, snr = 2, q=0.01, bgMode="manual", bg=[0])
            
        #save the restult image 
        #current_img.save(output_path+"/InputTest-"+str(idx)+".ics" , type="ics")
        result_img.save(output_path+"/OutputTest-"+str(idx)+".ics" , type="ics")
        
        del current_img
        del result_img      
    else :
        print (current_img_path + " doesn't exist!")
    
#elapsed = ttictoc.toc()
#print('Elapsed time:',elapsed)

print("DONE!")
