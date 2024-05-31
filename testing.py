# Script to automate drag and drop file

# options.add_argument("--start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")


# JS_DROP_FILE = """
# for(var b=arguments[0],k=arguments[1],l=arguments[2],c=b.ownerDocument,m=0;;){
#     var e=b.getBoundingClientRect(),
#         g=e.left+(k||e.width/2),
#         h=e.top+(l||e.height/2),
#         f=c.elementFromPoint(g,h);
#     if(f&&b.contains(f)) break;
#     if(1<++m) throw b=Error('Element not interractable'),b.code=15,b;
#     b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})
# }
# var a=c.createElement('INPUT');
# a.setAttribute('type','file');
# a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');
# a.onchange=function(){
#     var b={effectAllowed:'all',dropEffect:'none',types:['Files'],files:this.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};
#     window.DataTransferItemList&&(b.items=Object.setPrototypeOf([Object.setPrototypeOf({kind:'file',type:this.files[0].type,file:this.files[0],getAsFile:function(){return this.file},getAsString:function(b){var a=new FileReader;a.onload=function(a){b(a.target.result)};a.readAsText(this.file)}},DataTransferItem.prototype)],DataTransferItemList.prototype));
#     Object.setPrototypeOf(b,DataTransfer.prototype);
#     ['dragenter','dragover','drop'].forEach(function(a){
#         var d=c.createEvent('DragEvent');
#         d.initMouseEvent(a,!0,!0,c.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);
#         Object.setPrototypeOf(d,null);
#         d.dataTransfer=b;
#         Object.setPrototypeOf(d,DragEvent.prototype);
#         f.dispatchEvent(d)
#     });
#     a.parentElement.removeChild(a)
# };
# c.documentElement.appendChild(a);
# a.getBoundingClientRect();
# return a;
# """
# # input_field = driver.find_element(By.XPATH,'//input[@type="file"]')
# targetelement = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/div')
# filepath = "E:\\Work Projects\\mediustech\\Resume_ISHAN_BHARDWAJ.pdf"

# def drop_file(driver, target, file_path: str, offset_x: float = 0, offset_y: float = 0):
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(file_path)
    
#     js_executor = driver
#     input_element = js_executor.execute_script(JS_DROP_FILE, target, offset_x, offset_y)
#     input_element.send_keys(file_path)

# drop_file(driver,targetelement,filepath)