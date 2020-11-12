def transport(P1x,P1y,P2x,P2y,P3x,P3y,Tx,Ty):
    import matplotlib.pyplot as plt
    import numpy as np
    #=================================================== geting value's of user
    p1x = P1x
    p1y = P1y
    p2x = P2x
    p2y = P2y
    p3x = P3x
    p3y = P3y
    tx  = Tx
    ty  = Ty
    #=================================================== Calculations
    x   = [p1x, p2x, p3x, p1x]
    y   = [p1y, p2y, p3y, p1y]
    tx  = [p1x+tx, p2x+tx, p3x+tx, p1x+tx]
    ty  = [p1y+ty, p2y+ty, p3y+ty, p1y+ty]
    #=================================================== just for drawing good line's
    min_x  = int(min(x))
    min_tx = int(min(tx))
    min_y  = int(min(y))
    min_ty = int(min(ty))
    max_x  = int(max(x))
    max_tx = int(max(tx))
    max_y  = int(max(y))
    max_ty = int(max(ty))
    minix  = min(min_x,min_tx)
    maxix  = max(max_x,max_tx)
    miniy  = min(min_y,min_ty)
    maxiy  = max(max_y,max_ty)
    #=================================================== Drawing
    plt.plot(x, y, 'r-', color = 'w')
    plt.plot(tx, ty, 'r-', color = 'w')
    plt.fill(x, y, color = "green")
    plt.fill(tx, ty, color = "navy")
    plt.xticks(np.arange(minix - 3 ,maxix + 3, 1))
    plt.yticks(np.arange(miniy - 3 ,maxiy + 3, 1))
    plt.savefig('2D Transport.png')
    plt.close()
    # Araz Alinejad