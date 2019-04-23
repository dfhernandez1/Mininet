"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHosts1 = self.addHost( 'h1' )
        rightHosts1 = self.addHost( 'h2' )
        oSwitch = self.addSwitch( 's1' )

        # Add links
        self.addLink( leftHosts1, oSwitch )
	self.addLink( rightHosts1, oSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
