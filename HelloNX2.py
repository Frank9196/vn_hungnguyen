import NXOpen

def main():

    theSession  = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()

    #theSession.ListingWindow.Open()
    #/theSession.ListingWindow.WriteLine("Xin chào NX")
    theUI.NXMessageBox.Show("Xin Chào", NXOpen.NXMessageBox.DialogType.Information, "Xin chào NX")
    theUI.NXMessageBox.Show("Xin Chào", NXOpen.NXMessageBox.DialogType.Information, "Xin chào NX")
if __name__ == '__main__':
    main()