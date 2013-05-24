#!/usr/bin/env ruby
require "gtk2" 
Gtk.init

window = Gtk::Window.new("Karoshi Management")
window.set_default_size(350,50)
statusbar = Gtk::Statusbar.new
vbox = Gtk::VBox.new(false, 0)
#######################
#Main Menu
#######################
toolbar1 = Gtk::Toolbar.new.set_tooltips(true)
label1 = Gtk::Label.new("Karoshi Management")
hbox1 = Gtk::HBox.new(false, 10)
label1.set_alignment(0, 1)
#Main Menu icons
image1_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/bulk_user_creation.png")
image1_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/password.png")
image1_3 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/domain_info.png")
image1_4 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/printer.png")
image1_5 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/admin_file_browser.png")
#Main Menu Labels
tool_button1_1 = Gtk::ToolButton.new(image1_1, "User  ")
tool_button1_2 = Gtk::ToolButton.new(image1_2, "System")
tool_button1_3 = Gtk::ToolButton.new(image1_3, "Client")
tool_button1_4 = Gtk::ToolButton.new(image1_4, "Printer")
tool_button1_5 = Gtk::ToolButton.new(image1_5, "File")
toolbar1.append(tool_button1_1)
toolbar1.append(tool_button1_2)
toolbar1.append(tool_button1_3)
#toolbar1.append(tool_button1_4)
toolbar1.append(tool_button1_5)
#vbox.pack_start(label1)
vbox.pack_start(toolbar1)
vbox.pack_start(statusbar)

#######################
#User Management
#######################
label2 = Gtk::Label.new("User Management")
label2.set_alignment(0, 1)
toolbar2 = Gtk::Toolbar.new.set_tooltips(true)
toolbar3 = Gtk::Toolbar.new.set_tooltips(true)
toolbar4 = Gtk::Toolbar.new.set_tooltips(true)
#User Management icons
image2_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/copyfiles.png")
image2_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/groups.png")
image3_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
image4_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
#User Management labels
tool_button2_1 = Gtk::ToolButton.new(image2_1, "Copy\nDirectory\n")
tool_button2_2 = Gtk::ToolButton.new(image2_2, "Tidy\nStudent\nFiles")
tool_button3_1 = Gtk::ToolButton.new(image3_1, "\n\n")
tool_button4_1 = Gtk::ToolButton.new(image4_1, "\n\n")
toolbar2.append(tool_button2_1)
toolbar2.append(tool_button2_2)
toolbar3.append(tool_button3_1)
toolbar4.append(tool_button4_1)
#######################
#System Management
#######################
label5 = Gtk::Label.new("System Management")
label5.set_alignment(0, 1)
toolbar5 = Gtk::Toolbar.new.set_tooltips(true)
toolbar6 = Gtk::Toolbar.new.set_tooltips(true)
toolbar7 = Gtk::Toolbar.new.set_tooltips(true)
#System Management icons
image5_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/password.png")
image5_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/updateserver.png")
image5_3 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/network.png")
image5_4 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/backup.png")
image6_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/karoshi.png")
image6_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/karoshi.png")
image7_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/cron.png")
image7_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/vnc.png")
image7_4 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/shutdown.png")
#System Management labels
tool_button5_1 = Gtk::ToolButton.new(image5_1, "Change\nSystem\nPasswords")
tool_button5_2 = Gtk::ToolButton.new(image5_2, "Update\nServer\n")
tool_button5_3 = Gtk::ToolButton.new(image5_3, "Internet\nAccess\n")
tool_button5_4 = Gtk::ToolButton.new(image5_4, "Backup\nControls\n")
tool_button6_1 = Gtk::ToolButton.new(image6_1, "Apply\nKaroshi\nPatch")
tool_button6_2 = Gtk::ToolButton.new(image6_2, "Re-join\nKaroshi\nDomain")
tool_button7_1 = Gtk::ToolButton.new(image7_1, "Cron\nControls\n")
tool_button7_2 = Gtk::ToolButton.new(image7_2, "VNC\nRemote\nControl")
tool_button7_4 = Gtk::ToolButton.new(image7_4, "Shut\nDown \n")
toolbar5.append(tool_button5_1)
toolbar5.append(tool_button5_2)
toolbar5.append(tool_button5_3)
toolbar5.append(tool_button5_4)
toolbar6.append(tool_button6_1)
toolbar6.append(tool_button6_2)
toolbar7.append(tool_button7_1)
toolbar7.append(tool_button7_2)
toolbar7.append(tool_button7_4)
#######################
#Client Management
#######################
label8 = Gtk::Label.new("Client Management")
label8.set_alignment(0, 1)
toolbar8 = Gtk::Toolbar.new.set_tooltips(true)
toolbar9 = Gtk::Toolbar.new.set_tooltips(true)
toolbar10 = Gtk::Toolbar.new.set_tooltips(true)
#Client Management icons
image8_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/domain_info.png")
image8_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/deploy_windows_software.png")
image8_3 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/mirror_repository.png")
image9_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
image10_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
#Client Management labels
tool_button8_1 = Gtk::ToolButton.new(image8_1, "Domain\nInfo\n")
tool_button8_2 = Gtk::ToolButton.new(image8_2, "Deploy\nWindows\nSoftware")
tool_button8_3 = Gtk::ToolButton.new(image8_3, "Mirror\nLinux\nRepository")
tool_button9_1 = Gtk::ToolButton.new(image9_1, "\n\n")
tool_button10_1 = Gtk::ToolButton.new(image10_1, "\n\n")
toolbar8.append(tool_button8_1)
toolbar8.append(tool_button8_2)
toolbar8.append(tool_button8_3)
toolbar9.append(tool_button9_1)
toolbar10.append(tool_button10_1)
#######################
#File Management
#######################
label14 = Gtk::Label.new("File Management")
label14.set_alignment(0, 1)
toolbar14 = Gtk::Toolbar.new.set_tooltips(true)
toolbar15 = Gtk::Toolbar.new.set_tooltips(true)
toolbar16 = Gtk::Toolbar.new.set_tooltips(true)
#File Management icons
image14_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/quotas.png")
image14_2 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/hd.png")
image14_3 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/web_file_access.png")
image14_4 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/admin_file_browser.png")
image15_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
image16_1 = Gtk::Image.new("/opt/karoshi/serversetup/rubyicons/spacer.png")
#File Management labels
tool_button14_1 = Gtk::ToolButton.new(image14_1, "User\nDisk\nUsage")
tool_button14_2 = Gtk::ToolButton.new(image14_2, "Disk\nQuotas\n")
tool_button14_3 = Gtk::ToolButton.new(image14_3, "Web\nFile\nAccess")
tool_button14_4 = Gtk::ToolButton.new(image14_4, "Admin\nFile\nBrowser")
tool_button15_1 = Gtk::ToolButton.new(image15_1, "\n\n")
tool_button16_1 = Gtk::ToolButton.new(image16_1, "\n\n")

toolbar14.append(tool_button14_1)
toolbar14.append(tool_button14_2)
toolbar14.append(tool_button14_3)
toolbar14.append(tool_button14_4)
toolbar15.append(tool_button15_1)
toolbar16.append(tool_button16_1)

window.add(vbox)
window.border_width = 10
window.show_all

window.signal_connect("destroy") {
	Gtk.main_quit
}
#######################
#Button Commands Main Menu
#######################
#User Management
tool_button1_1.signal_connect("clicked") {
vbox.remove(label2)
vbox.remove(toolbar2)
vbox.remove(toolbar3)
vbox.remove(toolbar4)
vbox.remove(label5)
vbox.remove(toolbar5)
vbox.remove(toolbar6)
vbox.remove(toolbar7)
vbox.remove(label8)
vbox.remove(toolbar8)
vbox.remove(toolbar9)
vbox.remove(toolbar9)
vbox.remove(toolbar10)
vbox.remove(label14)
vbox.remove(toolbar14)
vbox.remove(toolbar15)
vbox.remove(toolbar16)

vbox.pack_start(label2)
vbox.pack_start(toolbar2)
vbox.pack_start(toolbar3)
vbox.pack_start(toolbar4)
window.show_all
}

#System Management
tool_button1_2.signal_connect("clicked") {
vbox.remove(label2)
vbox.remove(toolbar2)
vbox.remove(toolbar3)
vbox.remove(toolbar4)
vbox.remove(label5)
vbox.remove(toolbar5)
vbox.remove(toolbar6)
vbox.remove(toolbar7)
vbox.remove(label8)
vbox.remove(toolbar8)
vbox.remove(toolbar9)
vbox.remove(toolbar9)
vbox.remove(toolbar10)
vbox.remove(label14)
vbox.remove(toolbar14)
vbox.remove(toolbar15)
vbox.remove(toolbar16)

vbox.pack_start(label5)
vbox.pack_start(toolbar5)
vbox.pack_start(toolbar6)
vbox.pack_start(toolbar7)
window.show_all
}
#Client Management
tool_button1_3.signal_connect("clicked") {
vbox.remove(label2)
vbox.remove(toolbar2)
vbox.remove(toolbar3)
vbox.remove(toolbar4)
vbox.remove(label5)
vbox.remove(toolbar5)
vbox.remove(toolbar6)
vbox.remove(toolbar7)
vbox.remove(label8)
vbox.remove(toolbar8)
vbox.remove(toolbar9)
vbox.remove(toolbar9)
vbox.remove(toolbar10)
vbox.remove(label14)
vbox.remove(toolbar14)
vbox.remove(toolbar15)
vbox.remove(toolbar16)

vbox.pack_start(label8)
vbox.pack_start(toolbar8)
vbox.pack_start(toolbar9)
vbox.pack_start(toolbar10)
window.show_all
}

#File Management
tool_button1_5.signal_connect("clicked") {
vbox.remove(label2)
vbox.remove(toolbar2)
vbox.remove(toolbar3)
vbox.remove(toolbar4)
vbox.remove(label5)
vbox.remove(toolbar5)
vbox.remove(toolbar6)
vbox.remove(toolbar7)
vbox.remove(label8)
vbox.remove(toolbar8)
vbox.remove(toolbar9)
vbox.remove(toolbar10)
vbox.remove(label14)
vbox.remove(toolbar14)
vbox.remove(toolbar15)
vbox.remove(toolbar16)

vbox.pack_start(label14)
vbox.pack_start(toolbar14)
vbox.pack_start(toolbar15)
vbox.pack_start(toolbar16)
window.show_all
}

#######################
#Button Commands User Management
#######################
tool_button2_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/copyfilestoall &")
}

tool_button2_2.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/tidyfilecontrols &")
}

#######################
#Button Commands System Management
#######################

tool_button5_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/changemanagementpasswords &")
}

tool_button5_2.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/updateserver &")
}

tool_button5_3.signal_connect("clicked") {
	system("/opt/karoshi/serversetup/add_connection &")
}

tool_button5_4.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/backupcontrols &")
}

tool_button6_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/patch_karoshi &")
}

tool_button6_2.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/rejoin_domain &")
}

tool_button7_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/cronjobcontrols &")
}

tool_button7_2.signal_connect("clicked") {
	system("/opt/karoshi/serversetup/remotemanagement/vnccontrols &")
}

tool_button7_4.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/servershutdown &")
}

#######################
#Button Commands Client Management
#######################
tool_button8_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/domain_info &")
}


tool_button8_2.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/msimanagement &")
}

tool_button8_3.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/mirror_linux_client_repository &")
}

#######################
#Button Commands File Management
#######################
tool_button14_1.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/checkuserdiskusage &")
}

tool_button14_2.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/quotas_setup &")
}

tool_button14_3.signal_connect("clicked") {
	system("/opt/karoshi/serversetup/remote_file_access/setup_sslbridge &")
}

tool_button14_4.signal_connect("clicked") {
	system("/opt/karoshi/useful' 'scripts/admin_file_manager &")
}

Gtk.main