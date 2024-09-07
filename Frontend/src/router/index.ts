import { RouteRecordRaw, createRouter, createWebHistory } from "vue-router";

export const routes: Array<RouteRecordRaw> = [
    {
        path: "/",
        name: "landing",
        component: () => import("../pages/LandingPage/LandingPage.vue"),
    },
    {
        path: "/login",
        name: "login",
        component: () => import("../pages/Login/Login.vue"),
    },
    {
        path: "/signup",
        name: "singup",
        component: () => import("../pages/Signup/Signup.vue"),
    },
    {
        path: "/home",
        name: "homePage",
        component: () => import("../pages/HomePage/HomePage.vue"),
        children: [
            {
              path: "/home",
              name: "today",
              component: () => import("../pages/Today/Today.vue"),
            },
            {
                path: "/home/upcoming",
                name: "upcoming",
                component: () => import("../pages/Upcoming/Upcoming.vue"),
            },
            {
                path: "/home/stickywall",
                name: "stickywall",
                component: () => import("../pages/StickyWall/StickyWall.vue"),
            },
            {
                path: "/home/profile",
                name: "profile",
                component: () => import("../pages/Profile/Profile.vue"),
            },
            {
                path: "/home/:id",
                name: "selectedList",
                component: () => import("../pages/SelectedList/SelectedList.vue")
            }
        ]
    }
]
const router = createRouter({
    history: createWebHistory("/"),
    routes,
});

export default router;