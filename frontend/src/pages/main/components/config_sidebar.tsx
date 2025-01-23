import {
    BookOpen,
    Bot,
    Frame,
    Map,
    PieChart,
    // Settings2,
    SquareTerminal,
  } from "lucide-react"
  
// This is sample data.
export const config_menu = {
    navMain: [
      {
        title: "Playground",
        url: "#",
        icon: SquareTerminal,
        isActive: true,
        items: [
          {
            title: "Your Project",
            url: "/projects",
          }
        ],
      },
      {
        title: "Models",
        url: "#",
        icon: Bot,
        items: [
          {
            title: "Genesis",
            url: "#",
          },
          {
            title: "Explorer",
            url: "#",
          }
        ],
      },
      {
        title: "Libraries",
        url: "#",
        icon: BookOpen,
        items: [
          {
            title: "Your Libraries",
            url: "my-docs",
          },
          {
            title: "Debug - Your collections",
            url: "#",
          }
        ],
      },
    //   {
    //     title: "Settings",
    //     url: "#",
    //     icon: Settings2,
    //     items: [
    //       {
    //         title: "General",
    //         url: "#",
    //       },
    //       {
    //         title: "Team",
    //         url: "#",
    //       },
    //       {
    //         title: "Billing",
    //         url: "#",
    //       },
    //       {
    //         title: "Limits",
    //         url: "#",
    //       },
    //     ],
    //   },
    ],
    projects: [
      {
        name: "Design Engineering",
        url: "#",
        icon: Frame,
      },
      {
        name: "Sales & Marketing",
        url: "#",
        icon: PieChart,
      },
      {
        name: "Travel",
        url: "#",
        icon: Map,
      },
    ],
  }
  