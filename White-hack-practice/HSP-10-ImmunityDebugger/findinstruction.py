from immlib import *
def main(args):
    imm = Debugger()
    search_code = " ".join(args)
    search_bytes = imm.assemble( search_code )
    search_results = imm.search( search_bytes )
    count = 0
    for hit in search_results:
        # Retrieve the memory page where this hit exists
        # and make sure it's executable
        code_page = imm.getMemoryPageByAddress( hit )
        access = code_page.getAccess( human = True )
        if "execute" in access.lower():
            imm.log( "[*] Found: %s (0x%08x)" % ( search_code, hit ), address = hit )
            count += 1
    # return "[*] Finished searching for instructions, check the Log window."
    return "Found %d/%d addresses (Check the Log Windows for details)" % (count, len(search_results))
