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
        leftHosts2 = self.addHost( 'h2' )
	leftHosts3 = self.addHost( 'h3' )
	rightHosts1 = self.addHost( 'h4' )
        oSwitchLeft = self.addSwitch( 's1' )
	oSwitchRight = selg.addSwtich( 's2' )

        # Add links
        self.addLink( leftHosts1, oSwitchLeft )
	self.addLink( leftHosts2, oSwitchLeft )
	self.addLink( leftHosts3, oSwitchLeft )
	self.addLink( oSwitchLeft, oSwitchRight )
	self.addLink( oSwitchRight, rightHost1 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
