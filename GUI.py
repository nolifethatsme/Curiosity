{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red191\green100\blue38;\red32\green32\blue32;\red153\green168\blue186;
\red109\green109\blue109;\red160\green0\blue163;\red128\green63\blue122;\red254\green187\blue91;\red152\green54\blue29;
\red88\green118\blue71;\red95\green96\blue103;\red86\green132\blue173;}
{\*\expandedcolortbl;;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c60000\c65882\c72941;
\csgenericrgb\c42745\c42745\c42745;\csgenericrgb\c62745\c0\c63922;\csgenericrgb\c50196\c24706\c47843;\csgenericrgb\c99608\c73333\c35686;\csgenericrgb\c59608\c21176\c11373;
\csgenericrgb\c34510\c46275\c27843;\csgenericrgb\c37255\c37647\c40392;\csgenericrgb\c33725\c51765\c67843;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 import \cf4 tkinter \cf2 as \cf4 tk\
\
\
\cf5 # introduces page class for the frames to function.\
\cf2 class \cf4 page(tk.Frame):\
    \cf2 def \cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs):\
        tk.Frame.\cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs)\
\
    \cf2 def \cf8 show\cf4 (\cf7 self\cf4 ):\
        \cf7 self\cf4 .lift()\
\
\
\cf5 # users will be greeted with home page first and can then navigate via task bar at the top\
\cf2 class \cf4 home(page):\
    \cf2 def \cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs):\
        page.\cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs)\
        label = tk.Label(\cf7 self\cf2 , \cf9 text\cf4 =\cf10 "This is the home page/possibly a login page if we have time?"\cf4 )\
        label.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "both"\cf2 , \cf9 expand\cf4 =\cf2 True\cf4 )\
\
\
\cf5 # shows the page which is used for uploading/downloading by covering over the previous frame.\
\cf2 class \cf4 upload_download(page):\
    \cf2 def \cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs):\
        page.\cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs)\
        label = tk.Label(\cf7 self\cf2 , \cf9 text\cf4 =\cf10 "This is the download and upload page"\cf4 )\
        label.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "both"\cf2 , \cf9 expand\cf4 =\cf2 True\cf4 )\
\
        \cf5 # upload button, with placement\
        \cf11 upload_button \cf4 = tk.Button(\cf7 self\cf2 , \cf9 text\cf4 =\cf10 "Upload"\cf4 ).pack(\cf9 side\cf4 =\cf10 "left"\cf4 )\
\
\
\cf5 # this page will be used for automation as detailed in brief, connect to CMD/bash\
\cf2 class \cf4 command_line(page):\
    \cf2 def \cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs):\
        page.\cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs)\
        label = tk.Label(\cf7 self\cf2 , \cf9 text\cf4 =\cf10 "Command Line interface for automation"\cf4 )\
        label.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "both"\cf2 , \cf9 expand\cf4 =\cf2 True\cf4 )\
\
\
\cf5 # this will be visible throughout each page and will act as a menu bar at the top\
\cf2 class \cf4 main_view(tk.Frame):\
    \cf2 def \cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs):\
        tk.Frame.\cf6 __init__\cf4 (\cf7 self\cf2 , \cf4 *args\cf2 , \cf4 **kwargs)\
        p1 = home(\cf7 self\cf4 )\
        p2 = upload_download(\cf7 self\cf4 )\
        p3 = command_line(\cf7 self\cf4 )\
\
        button_frame = tk.Frame(\cf7 self\cf4 )\
        button_frame.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "x"\cf2 , \cf9 expand\cf4 =\cf2 False, \cf9 anchor\cf4 =\cf10 "center"\cf4 )\
        container = tk.Frame(\cf7 self\cf4 )\
        container.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "both"\cf2 , \cf9 expand\cf4 =\cf2 True\cf4 )\
\
        \cf5 # page placement\
        \cf4 p1.place(\cf9 in_\cf4 =container\cf2 , \cf9 x\cf4 =\cf12 0\cf2 , \cf9 y\cf4 =\cf12 0\cf2 , \cf9 relwidth\cf4 =\cf12 1\cf2 , \cf9 relheight\cf4 =\cf12 1\cf4 )\
        p2.place(\cf9 in_\cf4 =container\cf2 , \cf9 x\cf4 =\cf12 0\cf2 , \cf9 y\cf4 =\cf12 0\cf2 , \cf9 relwidth\cf4 =\cf12 1\cf2 , \cf9 relheight\cf4 =\cf12 1\cf4 )\
        p3.place(\cf9 in_\cf4 =container\cf2 , \cf9 x\cf4 =\cf12 0\cf2 , \cf9 y\cf4 =\cf12 0\cf2 , \cf9 relwidth\cf4 =\cf12 1\cf2 , \cf9 relheight\cf4 =\cf12 1\cf4 )\
\
        \cf5 # button creation... can make this look better with colours etc\
        \cf4 b1 = tk.Button(button_frame\cf2 , \cf9 text\cf4 =\cf10 "Home/Login"\cf2 , \cf9 command\cf4 =p1.show)\
        b2 = tk.Button(button_frame\cf2 , \cf9 text\cf4 =\cf10 "Upload/Download"\cf2 , \cf9 command\cf4 =p2.show)\
        b3 = tk.Button(button_frame\cf2 , \cf9 text\cf4 =\cf10 "Command Line"\cf2 , \cf9 command\cf4 =p3.show)\
\
        \cf5 # button placement and alignment\
        \cf4 b1.pack(\cf9 anchor\cf4 =\cf10 "center"\cf2 , \cf9 side\cf4 =\cf10 "left"\cf4 )\
        b2.pack(\cf9 anchor\cf4 =\cf10 "center"\cf2 , \cf9 side\cf4 =\cf10 "left"\cf4 )\
        b3.pack(\cf9 anchor\cf4 =\cf10 "center"\cf2 , \cf9 side\cf4 =\cf10 "left"\cf4 )\
\
        p1.show()\
\
\
\cf5 # the creation of the window... name can be changed\
\cf2 if \cf4 __name__ == \cf10 "__main__"\cf4 :\
    root = tk.Tk()\
    root.title(\cf10 "CuriosityFiles"\cf4 )\
    main = main_view(root)\
    main.pack(\cf9 side\cf4 =\cf10 "top"\cf2 , \cf9 fill\cf4 =\cf10 "both"\cf2 , \cf9 expand\cf4 =\cf2 True\cf4 )\
    root.wm_geometry(\cf10 "600x600"\cf4 )\
    root.mainloop()\
}