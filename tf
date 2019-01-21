#!/usr/bin/env bash

# driven by ~/bintest/apf     in ~/projects/apache
echo "Currently in " $PWD 
driver_cmd="djf"               # <<< CHANGE HERE name bintest/'wrapper'
# wrapper code - redirect to  ~/desired-dir/tj  passing parms
 # fall through replaces the else

if [ ".$1" == "." ]; then
    vim $0
    exit
  fi

listonly='no' 

sudo=""
if [ ".$2" == ".sudo" ]; then
  sudo="sudo"
fi
 
if [ ".." == ".$1" ]; then             # parm1 is .
    if [ ".$2" == ".list" ]; then      # parm2 is 'list'
       listonly='yes'
    fi
fi    

function goedit()
 {
   msg=""
   if [ -f $3 ]; then
      msg=" -- EXISTs."
   else
      msg=" -- does NOT Exist."
   fi

   if [ ".sudo" == ".$4" ]; then        # acro list indicates sudo
      sudo="sudo"
   fi

   if [ ".$listonly" == ".yes" ]; then
      echo $2 
      echo "..."$3 $msg
   elif [ ".$1" == ".$2" ]; then
      $sudo vim $3
   else
      return
   fi
 }
level1="nbdjango"
project="website"
app="music"

# fnt  parm1 acro      file
 goedit $1   notes     ~/$level1/rchnotes
 goedit $1   musicadmin ~/$level1/$project/$app/admin.py   sudo
 goedit $1   urls      ~/$level1/$project/website/urls.py  sudo
 goedit $1   musicurls ~/$level1/$project/$app/urls.py sudo
 goedit $1   musicviews ~/$level1/$project/$app/views.py sudo
 goedit $1   settings   ~/$level1/$project/website/settings.py sudo    
 goedit $1   musicmodels ~/$level1/$project/$app/models.py  sudo :    


if [ ".." != ".$1" ]; then 
    echo " >$1< as acronyn not found."
fi
    echo " "             # a blank line
    echo To show the list acro/file combo  enter  $driver_cmd . list
exit 0

# below is the wrapper function (set the desired dir var.) 
#!/usr/bin/env bash

# wrapper code - redirect to  ~/desired-dir/tf  passing parms

desired_dir="Where I am"    # <<< = change this:

if [ ".$PWD" != ".$desired_dir" ]; then   
   $HOME/$desired_dir/tf $1 $2 $3
   exit                  # really leave
fi
 # fall through replaces the else
echo "Should never see" 
